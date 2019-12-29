from __future__ import unicode_literals
from django.db import models

# 新增元组用于设置消息类型枚举类
KIND_CHOICES = (
    ('Python技术', 'Python技术'),
    ('数据库技术', '数据库技术'),
    ('经济学', '经济学'),
    ('文体咨询', '文体咨询'),
    ('个人心情', '个人心情'),
    ('其他', '其他'),
)


class Moment(models.Model):
    content = models.CharField('内容', max_length=300)
    user_name = models.CharField('username', max_length=20, default='匿名')
    # 修改kind定义，加入choices参数
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default=KIND_CHOICES[0])


# just test
LEVELS = (
    ('1', 'Very good'),
    ('2', 'Good'),
    ('3', 'Normal'),
    ('4', 'Bad'),
)


class Comment(models.Model):
    # id = models.AutoField(primary_key=True)
    # level = models.CharField(max_length=1, choices=LEVELS)
    # level = models.CharField('请为本条信息评级', max_length=1, choices=LEVELS)

    id = models.AutoField(primary_key=True)
    headline = models.CharField(max_length=255, default='default_headline')
    body_text = models.TextField(default='default_body')
    pub_date = models.DateField(auto_now=True)
    n_visits = models.IntegerField(default=99)

    def __str__(self):
        return self.headline


class Account(models.Model):
    user_name = models.CharField(max_length=80, null=True)
    password = models.CharField(max_length=255, null=True)
    reg_date = models.DateField(null=True)

    # def __unicode__(self):
    def __str__(self):
        return 'Account: %s' % self.user_name


class Contact(models.Model):
    # account = models.OneToOneField(
    #     Account,
    #     on_delete=models.CASCADE,
    #     primary_key=True,
    # )

    # account = models.ForeignKey(Account, on_delete=models.CASCADE)

    accounts = models.ManyToManyField(Account)
    zip_code = models.CharField(max_length=10)
    address = models.CharField(max_length=80)
    mobile = models.CharField(max_length=20)

    # def __unicode__(self):
    def __str__(self):
        return '%s, %s' % (self.account.user_name, self.mobile)
