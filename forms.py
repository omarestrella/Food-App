from django.forms import ModelForm
from models import Order

class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Order
        exclude = ["user", "date"]