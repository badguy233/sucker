from django.db import models

# Create your models here.
from login.models import *

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    utel = models.IntegerField()
    uaddress = models.CharField(max_length=200)
    ucreatetime = models.DateTimeField()
    loginID = models.OneToOneField(Login)

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