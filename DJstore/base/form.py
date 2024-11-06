from django.forms import ModelForm
from .models import Items
from .models import Orders

class ItemForm(ModelForm):
    class Meta:
        model = Items
        fields = ['category','name','price','description']

class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['location','method']