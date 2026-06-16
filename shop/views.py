from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def clear_cart(request):
    request.session['cart'] = {}

    return redirect('home')

def home(request):
    
    Products = Product.objects.all()

    cart = request.session.get('cart',{})

    return render(request, 'home.html', {
        'products': Products,
        'cart': cart
    })

def add_to_cart(request, product_id):
    cart = request.session.get('cart',{})

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1

    else:
        cart[product_id] = 1

    request.session['cart'] = cart

    return redirect('home')

def cart(request):

    cart = request.session.get('cart', {})

    products = Product.objects.filter(id__in=cart.keys())

    total = 0

    for product in products:

        total += product.price * cart[str(product.id)]


    return render(request, 'cart.html', {
        'products': products,
        'cart':cart,
        'total': total

    })

def increase_quantity(request, product_id):

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    cart[product_id] += 1

    request.session['cart'] = cart

    return redirect('cart')

def decrease_quantity(request, product_id):
    cart = request.session.get('cart',{})

    product_id = str(product_id)

    if product_id in cart:

        if cart[product_id] > 1:
            cart[product_id] -= 1
        else:
            del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart')

def remove_from_cart(request, product_id):

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:

        del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart')

def signup(request):
    form = UserCreationForm()

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('home')
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('home')
        
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)

    return redirect('home')

