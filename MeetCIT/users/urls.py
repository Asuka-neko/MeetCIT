from django.urls import path, include
from users.views import dashboard, register, homepage

app_name = 'users'
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', dashboard, name='dashboard'),
    path('register/', register, name='register'),
    path('homepage/', homepage, name='homepage'),
]
