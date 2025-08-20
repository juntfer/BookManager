from django.db import models

# Create your models here.
# 定义BookInfo表，继承models.Model类，dajango自动生成id字段，不需要手动设置
class BookInfo(models.Model):
    #在类中基于属性定义字段为name，类型为CharField，长度为20，unique=True，唯一
    name = models.CharField(max_length=20, unique=True,verbose_name='名称')
    #在类中基于属性定义字段为pub_date，类型为DateField，允许为空
    pub_date = models.DateField(verbose_name='发布日期',null=True)
    #在类中基于属性定义字段为readcount，类型为IntegerField，默认值为0
    readcount = models.IntegerField(default=0, verbose_name='阅读量')
    #在类中基于属性定义字段为commentcount，类型为IntegerField，默认值为0
    commentcount = models.IntegerField(default=0, verbose_name='评论量')
    #在类型基于属性定义字段为is_delete,逻辑删除字段，默认值为False
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    # 默认表的名字为：子应用名_类名（都是小写），在类中添加Meta类（必须为Meta）修改表的名称
    class Meta:
        # 修改表名
        db_table = 'bookinfo'
    #重写__str__方法，admin管理后台输出时返回name字段
    def __str__(self):
        return self.name

# 定义People表，继承models.Model类，dajango自动生成id字段，不需要手动设置
class People(models.Model):
    #定义有序字典，创建性别选项
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    # 在类中基于属性创建字段为name，类型为CharField，长度为20
    name = models.CharField(max_length=20, unique=True,verbose_name='名称')
    # 创建字段为gender，类型为SmallIntegerField，使用关键字choices设置可选项为GENDER_CHOICES
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    # 创建字段为description，类型为CharField，允许为空
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    # 创建字段为book，如果检测为外键类型，系统会自动将字段名添加_id,外键关联BookInfo
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    # 逻辑删除字段，默认值为False
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    #重写__str__方法，admin管理后台输出时返回name字段
    def __str__(self):
        return self.name

