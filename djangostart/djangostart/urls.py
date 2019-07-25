"""djangostart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

#导入的根路径是项目的根目录djangostart
from app01 import views
from django.conf.urls import include,url
import debug_toolbar

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #当路由过来，匹配上的时候，会执行视图的指定函数名 -》Django会给视图传递一个参数
    url(r'demo/$',views.demo),
    url(r'demo_form/$',views.demo_form),
    url(r'demo_form2/$',views.demo_form2),
    url(r'demo_form2_db/$',views.demo_form2_db),
]



