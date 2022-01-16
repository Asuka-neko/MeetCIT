from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from guardian.shortcuts import assign_perm
import calendar

from .models import *
from .utils import Calendar
from .forms import EventForm


def index(request):
    return render(request, 'homepage/index.html')


class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def catalogue(request):
    cur_user = User.objects.get(pk=request.user.id)
    earliest_slots_list = Event.objects.order_by(
        '-start_time').exclude(mentor=cur_user).exclude(available=False).exclude(start_time__lte=timezone.now())
    context = {'earliest_slots_list': earliest_slots_list}

    return render(request, 'homepage/catalogue.html', context)


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month


def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


@login_required
def event(request, event_id=None):
    cur_user = User.objects.get(pk=request.user.id)
    initial_data = {
        'mentor': cur_user
    }

    instance = Event()

    form = EventForm(request.POST or None,
                     instance=instance, initial=initial_data)
    if request.POST and form.is_valid():
        cur_event = form.save()
        # assign permission to the author
        assign_perm('cannot_book', cur_user, cur_event)
        assign_perm('can_edit', cur_user, cur_event)
        return HttpResponseRedirect(reverse('cal:calendar'))
    return render(request, 'cal/event.html', {'form': form})


@login_required
def event_edit(request, event_id=None):
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
        if request.user.has_perm('cal.can_edit', instance):
            cur_user = User.objects.get(pk=request.user.id)
            initial_data = {
                'mentor': cur_user,
                'zoom_link': instance.zoom_link,
                'start_time': instance.start_time,
                'end_time': instance.end_time
            }
            print(instance.zoom_link)
            form = EventForm(request.POST or None,
                             instance=instance, initial=initial_data)
            if request.POST and form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('cal:calendar'))
            return render(request, 'cal/event_edit.html', {'form': form})
        else:
            context = {
                'event_id': instance.pk,
                'mentor': instance.mentor,
                'zoom_link': instance.zoom_link,
                'start_time': instance.start_time,
                'end_time': instance.end_time,
                'is_available': instance.is_available(),
            }
            print(instance.is_available())
            return render(request, 'cal/event_view.html', context)


@login_required
def booksuccess(request, event_id):
    cur_user = User.objects.get(pk=request.user.id)
    instance = get_object_or_404(Event, pk=event_id)
    instance.available = False
    instance.mentee = cur_user
    instance.save()
    context = {
        'event_id': instance.pk,
        'mentor': instance.mentor,
        'zoom_link': instance.zoom_link,
        'start_time': instance.start_time,
        'end_time': instance.end_time,
        'is_available': instance.is_available(),
    }
    return render(request, 'cal/booksuccess.html', context)


@login_required
def profile(request):
    cur_user = User.objects.get(pk=request.user.id)
    user_event_expired = Event.objects.filter(mentee=cur_user).order_by(
        '-start_time').exclude(start_time__gte=timezone.now())
    user_event_upcoming = Event.objects.filter(mentee=cur_user).order_by(
        '-start_time').exclude(start_time__lte=timezone.now())

    context = {'user_event_expired': user_event_expired,
               'user_event_upcoming': user_event_upcoming,
               }

    return render(request, 'cal/profile.html', context)


@login_required
def cancelsuccess(request, event_id):
    instance = get_object_or_404(Event, pk=event_id)
    instance.available = True
    instance.mentee = None
    instance.save()
    context = {
        'event_id': instance.pk,
        'mentor': instance.mentor,
        'zoom_link': instance.zoom_link,
        'start_time': instance.start_time,
        'end_time': instance.end_time,
        'is_available': instance.is_available(),
    }
    return render(request, 'cal/cancelsuccess.html', context)
