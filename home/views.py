from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'home/about.html')
	
def work_clients(request):
	return render(request, 'home/page.html')
