from MySQLdb import connect
from django.shortcuts import render

# Create your views here.
# 引入HttpRequest和HttpResponse
from django.http import  HttpRequest
from django.http import  HttpResponse

#定义视图函数，至少定义一个参数必须用于接收用户请求
#这个请求其实就是HttpRequest的类对象，用于接收用户请求，一般命名为request
# 视图函数必须返回一个HttpResponse对象用于响应用户请求
def index(request):
    session1={"name":"王小明"}
    return render(request, 'book/index.html',context=session1)
