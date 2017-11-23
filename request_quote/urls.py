from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^request_quote/$', views.QuoteRequest.as_view(), name='quoteRequest'),
	#url(r'^quote/$', views.quote, name='quote'),
]