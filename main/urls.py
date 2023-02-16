from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('achivments', views.achivments, name='achivments'),
    path('items', views.items, name='items'),
    path('npc', views.npc, name='npc'),
    path('ships', views.ships, name='ships'),
    path('storytellings', views.storytellings, name='storytellings'),
]