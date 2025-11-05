from django.urls import path
#首先导入自定义的转换器类
from Converter.MobileConverter import MobileConverter
#导入注册转换器
from django.urls.converters import register_converter
from .views import index,getcookie,setsession,getsession
from .views import RegisterView
#注册路由转换器（自定义转换器类名、别名）
register_converter(MobileConverter, 'mobile')
urlpatterns=[
    #对接收路径参数占位符进行类型限制
    path('index/', index),
    path('cookie/',getcookie),
    path('session/', setsession),
    path('getsession/', getsession),
    path('register/',RegisterView.as_view()),
]

