#导入中间件父类
from django.utils.deprecation import MiddlewareMixin
#创建中间件类，继承MiddlewareMixin
class TestMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print("每次请求前调用执行此方法")
    def process_response(self, request, response):
        print("每次请求后调用执行此方法")
        return response