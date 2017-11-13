from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'contactus/contact.html')
	
def quote(request):
	return render(request, 'contactus/quotation.html')