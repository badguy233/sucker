from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

# Create your models here.
#shengyuan


class Login(models.Model):
    lname = models.CharField(max_length=20)
    lpassword = models.CharField(max_length=20)
    lemail = models.CharField(max_length=50)


class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    utel = models.IntegerField()
    uaddress = models.CharField(max_length=200)
    ucreatetime = models.DateTimeField()
    loginID = models.OneToOneField('Login')


class AddressInfo(models.Model):
    addrname = models.CharField(max_length=20)
    addrdetail = models.CharField(max_length=200)
    addrcode = models.IntegerField()
    addrtel = models.IntegerField()
    loginID = models.OneToOneField('UserInfo')


class OrderInfo(models.Model):
    number = models.CharField(max_length=20)
    userID = models.ForeignKey('UserInfo')
    detail = models.TextField(max_length=1000)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    delivery = models.DecimalField(max_digits=4, decimal_places=0)
    orderSum = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=200)
    datetime = models.DateTimeField()
    status = models.IntegerField()


class CartInfo(models.Model):
    goodID = models.IntegerField()
    userID = models.ForeignKey('UserInfo')
    qty = models.IntegerField()
    isDelete = models.BooleanField(default=False)


class GoodInfo(models.Model):
    gname = models.CharField(max_length=20)
    gdescrption = models.CharField(max_length=200)
    dictID = models.ForeignKey('Dict')
    gunit = models.CharField(max_length=20)
    gprice = models.CharField(max_length=20)
    gdetail = HTMLField()
    gpic = models.ImageField()


class Comment(models.Model):
    goodID = models.ForeignKey('GoodInfo')
    userID = models.ForeignKey('UserInfo')
    datetime = models.DateTimeField()
    content = models.CharField(max_length=100)


class ViewInfo(models.Model):
    ipAddr = models.CharField(max_length=20)
    goodID = models.ForeignKey('GoodInfo')


class Dict(models.Model):
    title = models.CharField(max_length=20)
    pid = models.ForeignKey('self', null=True, blank=True)
    isDelete = models.BooleanField(default=False)


class Log(models.Model):
	record = models.CharField(max_length=1000)
	datetime = models.DateTimeField()
