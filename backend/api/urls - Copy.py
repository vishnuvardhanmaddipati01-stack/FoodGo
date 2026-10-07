from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    RestaurantViewSet,
    FoodCategoryViewSet,
    FoodItemViewSet,
    CustomerViewSet,
    OrderViewSet
)


router = DefaultRouter()


router.register(
    'restaurants',
    RestaurantViewSet,
    basename='restaurant'
)


router.register(
    'categories',
    FoodCategoryViewSet,
    basename='category'
)


router.register(
    'foods',
    FoodItemViewSet,
    basename='food'
)


router.register(
    'customers',
    CustomerViewSet,
    basename='customer'
)


router.register(
    'orders',
    OrderViewSet,
    basename='order'
)


urlpatterns = router.urls