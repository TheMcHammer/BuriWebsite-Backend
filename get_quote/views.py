from django.views import generic 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Client

class IndexView(generic.ListView):
	template_name = "get_quote/index.html"
	context_object_name = "all_clients"
	
	def get_queryset(self):
		return Client.objects.all()
		
class DetailView(generic.DetailView):
	model = Client
	template_name = "get_quote/detail.html"
	
class ClientCreate(CreateView):
	model = Client
	fields = ['company','name','phone_num','address','email']
	
class ClientUpdate(UpdateView):
	model = Client
	fields = ['company','name','phone_num','address','email']
	
class ClientDelete(DeleteView):
	model = ClientCreate
	success_url = reverse_lazy('index.html')