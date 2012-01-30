from django.forms import ModelForm
from models import Order

class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        
        #instance = getattr(self, 'instance', None)
        #if instance and instance.id:
        #print 'asdf'
        self.fields['quantity'].widget.attrs['readonly'] = True

    def clean_quantity(self):
        return self.instance.quantity

    class Meta:
        model = Order
        exclude = ["user", "date"]