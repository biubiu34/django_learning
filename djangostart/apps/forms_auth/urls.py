from django.conf.urls import  url,include
from  . import views

urlpatterns = [
    url('^$',views.index,{"template_name":"forms_auth/index.html"},name='index'),
    url('^register/$', views.register,name='register'),
    url('^login/$', views.login, name='login'),
    url('^logout/$', views.logout, name='logout'),
]