from django.urls import re_path, path
from .views import booksuccess, index, CalendarView, event, event_edit, catalogue, profile, cancelsuccess

app_name = 'cal'
urlpatterns = [
    re_path(r'^index/$', index, name='index'),
    re_path(r'^calendar/$', CalendarView.as_view(), name='calendar'),
    re_path(r'^event/new/$', event, name='event_new'),
    re_path(r'^event/edit/(?P<event_id>\d+)/$',
            event_edit, name='event_edit'),
    path('homepage/', index, name='homepage'),
    re_path(r'^booksuccess/(?P<event_id>\d+)/$',
            booksuccess, name='booksuccess'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', profile, name='profile'),
    re_path(r'^cancelsuccess/(?P<event_id>\d+)/$',
            cancelsuccess, name='cancelsuccess'),
]
