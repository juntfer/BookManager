#导入Django自带的path函数，用于定义资源路径和视图函数
from django.urls import path
#导入当前子应用的视图函数
from .views import index
#定义当前子应用的资源路径和视图函数
urlpatterns=[
    path('index/', index),
]