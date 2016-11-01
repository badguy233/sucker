#coding=utf-8
from django.shortcuts import render

from . import models
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

#相信信息页数据的加载操作
def detail(request,id):
    good = models.GoodInfo.objects.get(pk=id)

    list1 = models.GoodInfo.objects.all()

    list2 = list1[0:2]

    dic = {
        'good':good,
        'list1':list2
    }

    return render(request, 'goods/detail.html',dic)


