from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'netfleet/network.html')
	
def fleet(request):
	return render(request, 'netfleet/fleet.html')