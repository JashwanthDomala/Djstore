from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Items
from .models import Orders
from .models import PayMethods

admin.site.register(Category)
admin.site.register(Items)
admin.site.register(Orders)
admin.site.register(PayMethods)
