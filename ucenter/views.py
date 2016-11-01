from django.shortcuts import render
from django.http import *
from models import *

# Create your views here.


def index(request):
    return render(request, 'index.html')


def user_center(request, pages):
	try:
		real_ip = request.META['HTTP_X_FORWARDED_FOR']
		regip = real_ip.split(",")[0]
	except:
		try:
			regip = request.META['REMOTE_ADDR']
		except:
			regip = ""
	if pages == '1':
		# name = request.session.get('uname')
		ucontent = UserInfo.objects.get(pk=1)
		gcontent = ViewInfo.objects.filter(ipAddr = '192.168.1.1')
        dict = {'uinfo': ucontent,'ginfo':gcontent}
        return render(request, 'user_center_info.html', dict)
	if pages == '2':
		return render(request, 'user_center_order.html')
	if pages == '3':
		return render(request, 'user_center_site.html')
