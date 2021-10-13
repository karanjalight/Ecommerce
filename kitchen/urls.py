from django.contrib import admin
from django.urls import path, include 
from core.views import Product,CheckoutView,Signup
from core.views import (
    remove_from_cart,
    reduce_quantity_item,
    add_to_cart,
    Home,
    OrderSummaryView,
    CheckoutView
)
from django.contrib.auth import views as auth_views

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', include('core.urls', namespace='core')), 
    path('', Home, name='home'),
    path('admin/', admin.site.urls),
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('logout', auth_views.LogoutView.as_view(template_name='home.html'), name="logout"),
    path('product/<int:pk>/', Product, name='product'),
    path('PaymentView/<int:pk>/', Product, name='product'),
  # path('Checkout/<int:pk>/', CheckoutView, name='checkout'),
    path('checkout', CheckoutView, name='checkout'),
    path('signup', Signup, name='signup'),
    

    path('order-summary', OrderSummaryView.as_view(), name='order-summary'),
    path('add-to-cart/<pk>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<pk>/', remove_from_cart, name='remove-from-cart'),
    path('reduce-quantity-item/<pk>/', reduce_quantity_item, name='reduce-quantity-item'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
   

]

# path('accounts/', include('django.contrib.auth.urls')),