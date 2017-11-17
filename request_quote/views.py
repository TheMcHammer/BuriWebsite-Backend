from .models import Quote
from django.views.generic.edit import CreateView

class QuoteRequest(CreateView):

	template_name = "request_quote/quote_form.html"
	model = Quote
	fields = ['commodity_type','packing_type','quantity','pick_from','deliver_to','is_clear_forward','company','name','phone_num','address','email']
	
