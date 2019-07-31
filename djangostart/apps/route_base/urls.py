
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^index2/$',views.index2,name='index2'),
    url(r'^zoos1/(\d+)/',views.zoos1,name="zoos1"),
    url(r'^zoos2/(?P<id>\d+)/',views.zoos2,name="zoos2"),
    url(r'^zoos3/(?P<id>\d+)/',views.zoos3,{"ty":"dog"},name="zoos3"),
    url(r'login/$',views.login,{'static':1},name="login")
]



