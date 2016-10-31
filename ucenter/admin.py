from django.contrib import admin
from models import *

# Register your models here.
class AdminLogin(admin.ModelAdmin):
	list_display = ['lname','lpassword','lemail']

class AdminLogin(admin.ModelAdmin):
	list_display = ['lname','lpassword','lemail']

class AdminUserInfo(admin.ModelAdmin):
	list_display = ['uname','utel','uaddress','ucreatetime','loginID']

class AdminAddressInfo(admin.ModelAdmin):
	list_display = ['addrname','addrdetail','addrcode','addrtel','loginID']

class AdminOrderInfo(admin.ModelAdmin):
	list_display = ['number','userID','detail','total','delivery','orderSum','address','datetime','status']

class AdminCartInfo(admin.ModelAdmin):
	list_display = ['goodID','userID','qty','isDelete']

class AdminGoodInfo(admin.ModelAdmin):
	list_display = ['gname','gdescrption','dictID','gunit','gprice','gdetail','gpic']

class AdminComment(admin.ModelAdmin):
	list_display = ['goodID','userID','datetime','content']

class AdminViewInfo(admin.ModelAdmin):
	list_display = ['ipAddr','goodID']

class AdminDict(admin.ModelAdmin):
	list_display = ['title','pid','isDelete']

class AdminLog(admin.ModelAdmin):
	list_display = ['record','datetime']

admin.site.register(Login,AdminLogin)
admin.site.register(UserInfo,AdminUserInfo)
admin.site.register(AddressInfo,AdminAddressInfo)
admin.site.register(OrderInfo,AdminOrderInfo)
admin.site.register(CartInfo,AdminCartInfo)
admin.site.register(GoodInfo,AdminGoodInfo)
admin.site.register(Comment,AdminComment)
admin.site.register(ViewInfo,AdminViewInfo)
admin.site.register(Dict,AdminDict)
admin.site.register(Log,AdminLog)