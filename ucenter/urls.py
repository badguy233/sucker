from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ucenter(?P<pages>[0-9]*)/$', views.user_center, name='user_center'),
]
