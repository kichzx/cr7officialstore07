

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

# def product_detail(request, product_id):
#     # Make sure your template is just 'product_detail.html' 
#     # and it is located inside your templates folder
#     product = get_object_or_404(Product, id=product_id)
#     return render(request, 'product_detail.html', {'product': product})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # If the file is just in 'templates/', use this:
    return render(request, 'product_detail.html', {'product': product})
    
    # OR, if you put it in 'templates/products/', use this instead:
    # return render(request, 'products/product_detail.html', {'product': product})

# def add_to_cart(request, product_id):
#     cart = request.session.get('cart', [])
#     if product_id not in cart:
#         cart.append(product_id)
#     request.session['cart'] = cart
#     return redirect('cart_page') # This points to the name in urls.py

def add_to_cart(request, product_id):
    # Initialize cart in session if it doesn't exist
    if 'cart' not in request.session:
        request.session['cart'] = []
    
    cart = request.session['cart']
    if product_id not in cart:
        cart.append(product_id)
        request.session.modified = True # Tell Django the session changed
    
    return redirect('cart_page') # This name MUST match your urls.py

def cart_view(request):
    cart_ids = request.session.get('cart', [])
    cart_items = Product.objects.filter(id__in=cart_ids)
    return render(request, 'cart.html', {'cart_items': cart_items})

# def remove_from_cart(request, product_id):
#     cart = request.session.get('cart', [])
#     if product_id in cart:
#         cart.remove(product_id)
#         request.session['cart'] = cart
#         request.session.modified = True
#     return redirect('cart_page') # Replace with your actual cart URL name

# views.py

# views.py
# from django.shortcuts import redirect

# def remove_from_cart(request, product_id):
#     # 1. Get the current cart from the session
#     cart = request.session.get('cart', [])

#     # 2. Convert ID to string (sessions usually store keys as strings)
#     product_id_str = str(product_id)

#     # 3. If the product exists in the cart, remove it
#     if product_id_str in cart:
#         cart.remove(product_id_str)
    
#     # 4. Save the updated cart back to the session
#     request.session['cart'] = cart
#     request.session.modified = True
    
#     # 5. Redirect the user back to the cart page
#     return redirect('cart_page') # Ensure this matches the 'name' in your urls.py


# from django.shortcuts import redirect

# def remove_from_cart(request, product_id):
#     # 1. Get the current cart list (or an empty list if it doesn't exist)
#     cart = request.session.get('cart', [])

#     # 2. Convert the ID to a string (Sessions often save data as strings)
#     product_id_str = str(product_id)

#     # 3. If found, remove it from the list
#     if product_id_str in cart:
#         cart.remove(product_id_str)
    
#     # 4. Save the new list back to the session
#     request.session['cart'] = cart
    
#     # 5. CRITICAL: Tell Django to save these changes to the database
#     request.session.modified = True
    
#     # 6. Go back to the cart page
#     return redirect('cart_page')

# def checkout(request):
#     cart_ids = request.session.get('cart', [])
#     # Get products from database based on IDs in session
#     products = Product.objects.filter(id__in=cart_ids)
    
#     # Calculate Total
#     total_price = sum(p.price for p in products)
    
#     return render(request, 'payment.html', {
#         'products': products,
#         'total_price': total_price
#     })

# from django.shortcuts import render
# from .models import Product

# def checkout(request):
#     # 1. Get IDs from the session cart
#     cart_ids = request.session.get('cart', [])
    
#     # 2. Fetch the actual product objects from the database
#     products = Product.objects.filter(id__in=cart_ids)
    
#     # 3. Calculate total for the payment page
#     total_price = sum(p.price for p in products)
    
#     return render(request, 'payment.html', {
#         'products': products, 
#         'total_price': total_price
#     })

from django.shortcuts import render, redirect
from .models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    if 'cart' not in request.session:
        request.session['cart'] = []
    
    cart = request.session['cart']
    if product_id not in cart:
        cart.append(product_id)
        request.session.modified = True 
    
    return redirect('cart_page')

def cart_view(request):
    cart_ids = request.session.get('cart', [])
    cart_items = Product.objects.filter(id__in=cart_ids)
    return render(request, 'cart.html', {'cart_items': cart_items})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])
    product_id_str = str(product_id)
    if product_id_str in cart:
        cart.remove(product_id_str)
    
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart_page')

def checkout(request):
    cart_ids = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart_ids)
    total_price = sum(p.price for p in products)
    
    return render(request, 'payment.html', {
        'products': products, 
        'total_price': total_price
    })