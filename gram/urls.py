from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name = 'index'),
    path('profile/', views.profile, name='profile'),
    path('upload/pic/', views.upload_pic, name = "upload_pic"),
    path('search/', views.search_results, name='search_results'),
    path('like/', views.like_image, name='like_image'),
    path('comments/<image_id>', views.comments,name='comments')
    ]
