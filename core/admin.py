from django.contrib import admin
from .models import Item, OrderItem, Order ,ProductImage,Sales

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Sales)
admin.site.register(ProductImage)
