from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^upload/pic/$', views.upload_pic, name = "upload_pic"),

]
