#coding=utf-8

# Create your models here.

from django.db import models
from tinymce.models import HTMLField
from ucenter.models import *

#商品信息
class GoodInfo(models.Model):
    gname = models.CharField(max_length=20)
    gdescrption = models.CharField(max_length=200)
    dictID = models.ForeignKey('Dict')
    gunit = models.CharField(max_length=20)
    gprice = models.DecimalField(max_digits=4, decimal_places=2)
    gdetail = HTMLField()
    gpic = models.ImageField(upload_to='uploads')


#字典（类型）
class Dict(models.Model):
    title = models.CharField(max_length=20)
    pid = models.ForeignKey('self', null=True, blank=True)
    path = models.CharField(max_length=100)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
       return self.title.encode('utf-8')


#评论信息
class Comment(models.Model):
    goodID = models.ForeignKey('GoodInfo')
    userID = models.ForeignKey(UserInfo)
    datetime = models.DateTimeField()
    content = models.CharField(max_length=100)


#浏览量
class ViewInfo(models.Model):
    ipAddr = models.CharField(max_length=20)
    goodID = models.ForeignKey('GoodInfo')
