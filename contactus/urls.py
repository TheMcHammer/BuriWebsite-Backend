from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^contactus/$', views.ContactCreate.as_view(), name='contact_add'),
	#url(r'^quote/$', views.quote, name='quote'),
]