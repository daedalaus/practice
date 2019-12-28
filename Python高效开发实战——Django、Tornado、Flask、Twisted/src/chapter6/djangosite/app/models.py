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
    content = models.CharField(max_length=300)
    user_name = models.CharField(max_length=20, default='匿名')
    # 修改kind定义，加入choices参数
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default=KIND_CHOICES[0])
