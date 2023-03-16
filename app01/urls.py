from django.urls import re_path as url
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.login,name='login'),
    url(r'^regist/$', views.regist,name='regist'),
    url(r'^index/$', views.index,name='index'),
    url(r'^index/(.\d+)/',views.book),
    url(r'^result/$', views.result,name='result'),

]