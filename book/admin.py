from django.contrib import admin

# Register your models here.
#导入models模块下的所有类（我们定义的模型）
from .models import BookInfo,People
#注册模型
admin.site.register(BookInfo)
admin.site.register(People)
