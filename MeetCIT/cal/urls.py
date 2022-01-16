from django.urls import re_path, path
from .views import booksucess, index, CalendarView, event, event_edit, catalogue

app_name = 'cal'
urlpatterns = [
    re_path(r'^index/$', index, name='index'),
    re_path(r'^calendar/$', CalendarView.as_view(), name='calendar'),
    re_path(r'^event/new/$', event, name='event_new'),
    re_path(r'^event/edit/(?P<event_id>\d+)/$',
            event_edit, name='event_edit'),
    path('homepage/', index, name='homepage'),
    re_path(r'^booksuccess/(?P<event_id>\d+)/$',
            booksucess, name='booksuccess'),
    path('catalogue/', catalogue, name='catalogue')
]
