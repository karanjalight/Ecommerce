from django.conf import settings
from django.db import models
from django.shortcuts import reverse

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

import cloudinary
from cloudinary.models import CloudinaryField




CATEGORY = (
    ('H', 'Electronics'),
    ('S', 'Cleaning and supplies'),
    ('O', 'Storage Supplies'),
    ('C', 'Cuttleries'),
    ('B', 'Bathroom'),
    ('E', 'Beddings'),
    
)

LABEL = (
    ('N', 'New'),
    ('BS', 'Best Seller')
)

class Item(models.Model):
    item_name = models.CharField(max_length=100)
    image = CloudinaryField('image')
    #image=cloudinary.models.CloudinaryField('image')
    #image = models.ImageField(upload_to="products/")
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY, max_length=20)
    label = models.CharField(choices=LABEL, max_length=2)
    description = models.TextField()

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            "pk" : self.pk
        
        })

    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            "pk" : self.pk
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            "pk" : self.pk
        })










class ProductImage(models.Model):
    item_name = models.CharField(max_length=100)
    
    item = models.ForeignKey(Item, on_delete=models.CASCADE)  
    image = models.ImageField(upload_to="products/images/")

    def __str__ (self):
        return self.item_name

class CheckoutAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100,null=True)
  

  

    def __str__(self):
        return self.user.username


class Sales(models.Model):
    customer_name = models.CharField(max_length=50)
    number = models.CharField(max_length=10)
    location = models.CharField(max_length=20)
    
 

    def __str__ (self):
        return self.customer_name
    
        
    

class OrderItem(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.item_name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_discount_item_price()
        return self.get_total_item_price()
    
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    checkout_address = models.ForeignKey(
        'CheckoutAddress', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total




class Payment(models.Model):
    stripe_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, 
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
