from django.forms import ModelForm
from .models import Sales,Item
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

PAYMENT = (
    ('C', 'Cash'),
    ('M', 'M-pesa')
)

class CheckoutForm(ModelForm): 
    class Meta:
         model = Sales
         fields = ["customer_name", "number", "location"]
         labels = {'customer_name':"Name", 'number': "number", 'location': "Location"}

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']