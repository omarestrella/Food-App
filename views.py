from django.views.generic import TemplateView, ListView
from models import Item, Order
from forms import OrderForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

class HomepageView(TemplateView):
    template_name = 'foodapp/homepage.html'

class ItemListView(ListView):
	template_name = 'items.html'
	model = Item
	context_object_name = 'items'

class OrderListView(ListView):
	template_name = 'orders.html'
	model = Order
	context_object_name = 'orders'

class OrderFormView(FormView):
	template_name = 'placeOrder.html'
	form_class = forms.OrderForm
	success_url = 'directory'
