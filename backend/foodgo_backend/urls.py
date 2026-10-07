from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [

    # HOME → LOGIN
    path(
        '',
        TemplateView.as_view(
            template_name='login.html'
        ),
        name='home'
    ),

    # ADMIN
    path(
        'admin/',
        admin.site.urls
    ),

    # API
    path(
        'api/',
        include('api.urls')
    ),

    # LOGIN
    path(
        'login/',
        TemplateView.as_view(
            template_name='login.html'
        ),
        name='login'
    ),

    # REGISTER
    path(
        'register/',
        TemplateView.as_view(
            template_name='register.html'
        ),
        name='register'
    ),

    # RESTAURANTS
    path(
        'restaurants/',
        TemplateView.as_view(
            template_name='restaurants.html'
        ),
        name='restaurants'
    ),

    # RESTAURANT MENU
    path(
        'restaurant/',
        TemplateView.as_view(
            template_name='restaurant.html'
        ),
        name='restaurant'
    ),

    # CART
    path(
        'cart/',
        TemplateView.as_view(
            template_name='cart.html'
        ),
        name='cart'
    ),

    # CHECKOUT
    path(
        'checkout/',
        TemplateView.as_view(
            template_name='checkout.html'
        ),
        name='checkout'
    ),

    # ORDERS
    path(
        'orders/',
        TemplateView.as_view(
            template_name='orders.html'
        ),
        name='orders'
    ),

    # PROFILE
    path(
        'profile/',
        TemplateView.as_view(
            template_name='profile.html'
        ),
        name='profile'
    ),

]