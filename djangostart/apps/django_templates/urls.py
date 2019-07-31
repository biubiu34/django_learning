from django.conf.urls import url
from . import views

urlpatterns = [
    #直接匹配jango_templates
    url(r'^$', views.index, name="index"),
]