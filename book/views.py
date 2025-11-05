from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.deprecation import MiddlewareMixin

def index(request):
    response = HttpResponse('ok')
    # 设置cookie信息
    response.set_cookie('username', 'zhangsan', max_age=3600)
    return response


def getcookie(request):
    response = HttpResponse('获取cookie信息')
    # 设置cookie信息
    cookie1 = request.COOKIES.get('username')
    print("cookie信息为：", cookie1)
    return response


def delcookie(request):
    response = HttpResponse('ok')
    # 删除cookie信息
    response.delete_cookie('name')
    return response


def setsession(request):
    response = HttpResponse('ok')
    # 设置session信息
    request.session['username'] = 'lisi'
    #设置session的过期时间
    request.session.set_expiry(3600)
    return response


def getsession(request):
    response = HttpResponse('ok')
    # 获取session信息
    username = request.session.get("username")
    print("session信息为：", username)
    return response

class RegisterView(LoginRequiredMixin,View,MiddlewareMixin):
    # 处理请求前自动调用
    def process_request(self, request):
        print('process_request1 被调用')
    # 处理视图前自动调用
    def process_view(self, request, view_func, view_args, view_kwargs):
        print('process_view1 被调用')
    def process_response(self, request, response):
        print('process_response1 被调用')
        return response
    def get(self,request):
        return HttpResponse('get请求返回报文')
    def post(self, request):
        return HttpResponse('post请求返回报文')














