from django.db import models

# Create your models here.
from ucenter.models import *



class CartInfo(models.Model):
    goodID = models.IntegerField()
    userID = models.ForeignKey(UserInfo)
    qty = models.IntegerField()
    isDelete = models.BooleanField(default=False)


class Log(models.Model):
    record = models.CharField(max_length=1000)
    datetime = models.DateTimeField()