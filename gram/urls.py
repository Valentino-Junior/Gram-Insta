from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^upload/pic/$', views.upload_pic, name = "upload_pic"),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^comment/(?P<image_id>\d+)', views.comment,name = "comment"),



]
