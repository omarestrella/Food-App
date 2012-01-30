from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView

from models import Item, Order
from forms import OrderForm

class HomepageView(CreateView):
    template_name = 'foodapp/placeOrder.html'
    form_class = forms.OrderForm
    success_url = 'foodapp/order.html'

class OrderListView(ListView):
    template_name = 'foodapp/orders.html'
    model = Order
    context_object_name = 'orders'