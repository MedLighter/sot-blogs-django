from django.urls import path
from . import views


app_name='blogs'

urlpatterns = [
    path('news/', views.news, name='news'),
    path('new-art/', views.new_art, name='new_art'),
    path('article/detail/<int:article_id>/', views.article_detail, name='article_detail'),
    path('personal-aricle/', views.personal_article, name='personal_article'),
    path('delete-article/<int:article_id>', views.delete_article, name='delete_article'),
    path('delete-comment/<int:comment_id>', views.delete_comment, name='delete_comment'),
]