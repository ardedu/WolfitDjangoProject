from django.contrib import admin

# Register your models here.

from .models import Cart
from .models import CartItem
from .models import Product

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
