from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.create,name='create'),
    path('<int:article_pk>/',views.detail,name='detail'),
    path('<int:article_pk>/update/',views.update,name='update'),
    path('<int:article_pk>/delete/',views.delete,name='delete'),
    path('<int:article_pk>/comments_create/',views.comments_create,name='comments_create'),
    path('<int:article_pk>/comment_delete/<int:comment_pk>/',views.comment_delete,name='comment_delete'),
    path('<int:article_pk>/like/',views.like,name='like'),
]
