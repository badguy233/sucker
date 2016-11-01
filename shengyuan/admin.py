from django.contrib import admin
from models import *

# Register your models here.
class AdminCartInfo(admin.ModelAdmin):
    list_display = ['goodID','userID','qty','isDelete']

class AdminLog(admin.ModelAdmin):
    list_display = ['record','datetime']


admin.site.register(CartInfo,AdminCartInfo)
admin.site.register(Log,AdminLog)