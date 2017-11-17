from .models import Contact
from django.views.generic.edit import CreateView

class ContactCreate(CreateView):
    model = Contact
    fields = ['first_name','second_name','address','county','town','email','comment']
	
	
