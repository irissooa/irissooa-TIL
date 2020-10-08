from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('',views.index,name='index'),
    path('reviews/',views.review_list,name='review_list'),
    path('reviews/create/',views.create,name='create'),
    path('reviews/<int:review_pk>/',views.review_detail,name='review_detail'),
    path('reviews/<int:review_pk>/comments/',views.comments,name='comments'),
    path('reviews/<int:review_pk>/like/',views.like,name='like'),
    path('reviews/<int:review_pk>/like/<int:comment_pk>',views.like_comment,name='like_comment'),
]
