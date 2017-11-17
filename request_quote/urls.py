from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.QuoteRequest.as_view(), name='QuoteRequest'),
	#url(r'^quote/$', views.quote, name='quote'),
]