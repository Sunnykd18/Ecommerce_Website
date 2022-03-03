from django.urls import path

from .views import (
    products,
    checkout,
    ItemDetailView,
    add_to_cart,
    remove_from_cart
)
from . views import home

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('checkout/', checkout, name='checkout'),
    path('products/', products, name='products'),
    path('products/<slug>/', ItemDetailView.as_view(), name='product-detail'),
    path('add-to-cart/<slug>/', add_to_cart,name = 'add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart,name = 'remove-from-cart')
]
