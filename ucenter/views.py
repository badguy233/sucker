from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'index.html')

def user_center(request,pages):
	if pages=='' or pages =='1':
		return render(request,'user_center_info.html')
	if pages =='2':
		return render(request,'user_center_order.html')
	if pages =='3':
		return render(request,'user_center_site.html')