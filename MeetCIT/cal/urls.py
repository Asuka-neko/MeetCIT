from django.urls import re_path, path
from .views import index, CalendarView, event, homepage

app_name = 'cal'
urlpatterns = [
<<<<<<< HEAD
    re_path(r'^index/$', index, name='index'),
    re_path(r'^calendar/$', CalendarView.as_view(), name='calendar'),
    re_path(r'^event/new/$', event, name='event_new'),
    re_path(r'^event/edit/(?P<event_id>\d+)/$',
            event, name='event_edit'),
    path('homepage/', homepage, name='homepage'),
=======
    re_path(r'^index/$', views.index, name='index'),
    re_path(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    re_path(r'^event/new/$', views.event, name='event_new'),
    re_path(r'^event/edit/(?P<event_id>\d+)/$', views.event_edit, name='event_edit'),
>>>>>>> main
]
