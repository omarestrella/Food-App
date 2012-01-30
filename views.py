from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView

import datetime

from models import Item, Order
from forms import OrderForm

from django.utils.functional import lazy
from django.core.urlresolvers import reverse
# Workaround for using reverse with success_url in class based generic views
# because direct usage of it throws an exception.
reverse_lazy = lambda name=None, *args : lazy(reverse, str)(name, args=args)

class HomepageView(CreateView):
    form_class = OrderForm
    success_url = reverse_lazy('url_orders')
    template_name = 'foodapp/homepage.html'
    object = Order

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)

        if form.is_valid():
            self.object = form.save(commit=False)
            item = Item.objects.get(pk=request.POST.get("item"))

            if item.once_a_day:
                try:
                    ordered = Order.objects.filter(user=request.user).get(item__pk=request.POST.get("item"), date=datetime.date.today)
                except Order.DoesNotExist:
                    return self.render_to_response(self.get_context_data(form=form))
                
                if ordered:
                    return self.render_to_response(self.get_context_data({"form": form, "error": "This item has already been ordered"}))
            else:
                return self.render_to_response(self.get_context_data(form=form))
        else:
            return self.render_to_response(self.get_context_data(form=form))

class OrderListView(ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'foodapp/orders.html'