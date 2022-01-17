from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from guardian.shortcuts import assign_perm
import calendar

from .models import *
from .utils import Calendar
from .forms import EventForm


def index(request):
    return render(request, 'homepage/index.html')


class SearchResultsView(ListView):
    model = Event
    template_name = 'homepage/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        cur_user = User.objects.get(pk=self.request.user.id)
        event_list = Event.objects.filter(host=query).order_by('start_time').exclude(
            available=False).exclude(start_time__lte=timezone.now()).exclude(host=cur_user)
        return event_list


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
    if request.user.is_authenticated:
        cur_user = User.objects.get(pk=request.user.id)
        earliest_slots_list = Event.objects.order_by(
            'start_time').exclude(host=cur_user).exclude(available=False).exclude(start_time__lte=timezone.now())
        context = {'earliest_slots_list': earliest_slots_list}
        return render(request, 'homepage/catalogue.html', context)
    else:
        earliest_slots_list = Event.objects.order_by(
            'start_time').exclude(available=False).exclude(start_time__lte=timezone.now())
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
        'host': cur_user
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
                'host': cur_user,
                'zoom_link': instance.zoom_link,
                'start_time': instance.start_time,
                'end_time': instance.end_time,
                'event_id': instance.pk,
            }

            form = EventForm(request.POST or None,
                             instance=instance, initial=initial_data)
            if request.POST and form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('cal:calendar'))
            return render(request, 'cal/event_edit.html', {'form': form, 'instance': initial_data})
        else:
            cur_user = User.objects.get(pk=request.user.id)
            can_cancel = (cur_user == instance.mentee)
            context = {
                'event_id': instance.pk,
                'host': instance.host,
                'zoom_link': instance.zoom_link,
                'start_time': instance.start_time,
                'end_time': instance.end_time,
                'is_available': instance.is_available(),
                'can_cancel': can_cancel,
            }
            print(instance.is_available())
            print(timezone.now())
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
        'host': instance.host,
        'zoom_link': instance.zoom_link,
        'start_time': instance.start_time,
        'end_time': instance.end_time,
        'is_available': instance.is_available(),
    }
    return render(request, 'cal/booksuccess.html', context)


@login_required
def profile(request):
    cur_user = User.objects.get(pk=request.user.id)

    host_event_expired = Event.objects.filter(host=cur_user).order_by(
        'start_time').exclude(start_time__gte=timezone.now())
    host_event_upcoming = Event.objects.filter(host=cur_user).order_by(
        'start_time').exclude(start_time__lte=timezone.now())

    user_event_expired = Event.objects.filter(mentee=cur_user).order_by(
        'start_time').exclude(start_time__gte=timezone.now())
    user_event_upcoming = Event.objects.filter(mentee=cur_user).order_by(
        'start_time').exclude(start_time__lte=timezone.now())

    context = {'host_event_expired': host_event_expired,
               'host_event_upcoming': host_event_upcoming,
               'user_event_expired': user_event_expired,
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
        'host': instance.host,
        'zoom_link': instance.zoom_link,
        'start_time': instance.start_time,
        'end_time': instance.end_time,
        'is_available': instance.is_available(),
    }
    return render(request, 'cal/cancelsuccess.html', context)


@login_required
def cancelhostsuccess(request, event_id):
    instance = get_object_or_404(Event, pk=event_id)
    context = {
        'host': instance.host,
        'mentee': instance.mentee,
        'start_time': instance.start_time,
    }
    instance.delete()
    return render(request, 'cal/cancelhostsuccess.html', context)
