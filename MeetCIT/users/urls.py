from django.urls import path, include, re_path
from users.views import register

app_name = 'users'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
]
