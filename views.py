from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView

from models import Item, Order
from forms import OrderForm

class HomepageView(CreateView):
    form_class = OrderForm
    success_url = 'foodapp/order.html'
    template_name = 'foodapp/homepage.html'

class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'foodapp/orders.html'