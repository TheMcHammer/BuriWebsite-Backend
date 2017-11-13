from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^work_clients/$', views.work_clients, name='work_clients'),
]