from django.urls import path
from . import views


app_name='blogs'

urlpatterns = [
    path('news/', views.news, name='news'),
    path('new-art/', views.new_art, name='new_art'),
    path('article/detail/<int:article_id>/', views.article_detail, name='article_detail')
]