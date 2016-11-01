# coding=utf-8

from django.contrib import admin

# Register your models here.
from models import *

# 进行对应admin数据的绑定操作

#产品信息展示
class AdminGoodInfo(admin.ModelAdmin):
    list_display = ['gname', 'gdescrption',
                    'dictID', 'gunit', 'gprice', 'gdetail', 'gpic']


# 字典信息展示
class AdminDict(admin.ModelAdmin):
    list_display = ['title', 'pid', 'path', 'isDelete']


#访问量管理
class AdminViewInfo(admin.ModelAdmin):
    list_display = ['ipAddr','goodID']


#评论信息管理
class AdminComment(admin.ModelAdmin):
    list_display = ['goodID','userID','datetime','content']



# 产品信息和字典（产品类型）
admin.site.register(GoodInfo,AdminGoodInfo)
admin.site.register(Dict,AdminDict)

# 评论和浏览量
admin.site.register(Comment,AdminComment)
admin.site.register(ViewInfo,AdminViewInfo)
