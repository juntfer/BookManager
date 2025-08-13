from django.db import models

# Create your models here.
# 定义BookInfo表，继承models.Model类，dajango自动生成id字段，不需要手动设置
class BookInfo(models.Model):
    # 定义字段为name，类型为CharField，长度为100
    name = models.CharField(max_length=100)
    #重写__str__方法，输出时返回name字段
    def __str__(self):
        return self.name

# 定义People表，继承models.Model类，dajango自动生成id字段，不需要手动设置
class People(models.Model):
    # 定义字段为name，类型为CharField，长度为100
    name = models.CharField(max_length=100)
    # 定义字段为gender，类型为BooleanField
    gender = models.BooleanField()
    # 定义字段为book，类型为ForeignKey，外键关联Book表
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    #重写__str__方法，输出时返回name字段
    def __str__(self):
        return self.name
