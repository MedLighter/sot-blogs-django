from django.urls import path
from . import views


app_name='users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('regitration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile')
]