# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home),
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     # This <int:product_id> captures the ID of the product you clicked
#     path('product/<int:product_id>/', views.product_detail, name='product_detail'),
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('product/<int:product_id>/', views.product_detail, name='product_detail'),
#     path('cart/', views.cart_view, name='cart_page'), 
#     path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('product/<int:product_id>/', views.product_detail, name='product_detail'),
#     path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
#     path('cart/', views.cart_view, name='cart_page'), # Make sure this is 'cart_page'
#     path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
#     path('checkout/', views.checkout, name='checkout'),]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('product/<int:product_id>/', views.product_detail, name='product_detail'),
#     path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    
#     # 1. This must match the name in your cart.html
#     path('cart/', views.cart_view, name='cart_page'),
    
#     # 2. This must match the remove logic in your views.py
#     path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    
#     path('checkout/', views.checkout, name='checkout'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_page'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
]