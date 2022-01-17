from django.urls import re_path, path
from .views import booksuccess, index, CalendarView, event, event_edit, catalogue, profile, cancelsuccess, cancelhostsuccess, SearchResultsView

app_name = 'cal'
urlpatterns = [
    re_path(r'^calendar/$', CalendarView.as_view(), name='calendar'),
    re_path(r'^event/new/$', event, name='event_new'),
    re_path(r'^event/edit/(?P<event_id>\d+)/$',
            event_edit, name='event_edit'),
    path('', index, name='homepage'),
    re_path(r'^booksuccess/(?P<event_id>\d+)/$',
            booksuccess, name='booksuccess'),
    path('catalogue/', catalogue, name='catalogue'),
    path('profile/', profile, name='profile'),
    re_path(r'^cancelsuccess/(?P<event_id>\d+)/$',
            cancelsuccess, name='cancelsuccess'),
    re_path(r'^cancelhostsuccess/(?P<event_id>\d+)/$',
            cancelhostsuccess, name='cancelhostsuccess'),
    path('search_results/', SearchResultsView.as_view(), name='search_results')
]
