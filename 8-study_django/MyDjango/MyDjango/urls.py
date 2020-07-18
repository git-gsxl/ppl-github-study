"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App_xl import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello_demo),
    url(r'^json/$', views.json_demo),   # 推荐 url 写法
    url(r'^login/$', views.login_demo),
    # path("login/<name>/<phone>", views.json_demo),
    # url(r"^login/(？P<code>[0-9]{2})/(？P<phone>[0-9]{11}", views.json_demo),
    url(r'^loginapp/aa/(?P<year>[0-9]{4})/(?P<month>[0-9]{2}).study_html$', views.json_demo)
]
