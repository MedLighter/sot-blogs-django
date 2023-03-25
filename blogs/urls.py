from django.urls import path
from . import views


app_name='blogs'

urlpatterns = [
    path('news/', views.news, name='news'),
    path('new-art/', views.new_art, name='new_art')
]