from django.contrib import admin
from models import *

# Register your models here.
class AdminUserInfo(admin.ModelAdmin):
    list_display = ['uname','utel','uaddress','ucreatetime','loginID']

class AdminAddressInfo(admin.ModelAdmin):
    list_display = ['addrname','addrdetail','addrcode','addrtel','loginID']

class AdminOrderInfo(admin.ModelAdmin):
    list_display = ['number','userID','detail','total','delivery','orderSum','address','datetime','status']


admin.site.register(UserInfo,AdminUserInfo)
admin.site.register(AddressInfo,AdminAddressInfo)
admin.site.register(OrderInfo,AdminOrderInfo)