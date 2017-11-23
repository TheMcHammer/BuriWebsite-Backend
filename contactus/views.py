from .models import Contact
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class ContactCreate(CreateView):
    model = Contact
    fields = ['first_name','second_name','address','county','town','email','comment']
    template_name='contactus/contact_form.html'