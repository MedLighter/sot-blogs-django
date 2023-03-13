from django.urls import path
from . import views


app_name='main'

urlpatterns = [
    path('', views.index, name='index'),
    path('achivments/', views.achivments, name='achivments'),
    path('items/chests/', views.items_chests, name='items_chests'),
    path('items/weapons/', views.items_weapons, name='items_weapons'),
    path('npc/', views.npc, name='npc'),
    path('ships/', views.ships, name='ships'),
    path('storytellings/seasons/', views.storytellings_seasons, name='storytellings_seasons'),
    path('storytellings/TallTales/', views.storytellings_TallTales, name='storytellings_TallTales')
]

