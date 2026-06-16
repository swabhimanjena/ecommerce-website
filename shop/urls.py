from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path(
        'add-to-cart/<int:product_id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),

    path(
        'cart/',
        views.cart,
        name='cart'
    ),

    path(
        'remove-from-cart/<int:product_id>/',
        views.remove_from_cart,
        name='remove_from_cart'
    ),

    path(
        'signup/',
        views.signup,
        name='signup'
    ),

    path(
        'login/',
        views.user_login,
        name='login'
    ),

    path(
        'logout/',
        views.user_logout,
        name='logout'
    ),

    path(
        'clear-cart/',
        views.clear_cart,
        name='clear_cart'
    ),

    path(
        'decrease-quantity/<int:product_id>/',
        views.decrease_quantity,
        name='decrease_quantity'
    ),

    path(
        'increase-quantity/<int:product_id>/',
        views.increase_quantity,
        name='increase_quantity'
    ),

]