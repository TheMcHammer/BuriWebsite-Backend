from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.ContactCreate.as_view(), name='ContactCreate'),
	#url(r'^quote/$', views.quote, name='quote'),
]