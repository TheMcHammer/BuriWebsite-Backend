from django.conf.urls import url
from . import views

app_name = 'get_quote'

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
	
	url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(), name='detail'),
	# /get_quote/client/add/
	url(r'client/add/$', views.ClientCreate.as_view(), name='client-add'),

	url(r'client/(?P<pk>[0-9]+)/$', views.ClientUpdate.as_view(), name='client-update'),

	url(r'client/(?P<pk>[0-9]+)/delete/$', views.ClientDelete.as_view(), name='client-delete'),
]
