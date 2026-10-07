from datetime import timedelta

from django.utils import timezone
from rest_framework import viewsets

from .models import (
    Restaurant,
    FoodCategory,
    FoodItem,
    Customer,
    Order
)

from .serializers import (
    RestaurantSerializer,
    FoodCategorySerializer,
    FoodItemSerializer,
    CustomerSerializer,
    OrderSerializer
)


class RestaurantViewSet(viewsets.ModelViewSet):

    queryset = Restaurant.objects.filter(
        is_active=True
    ).order_by('-rating')

    serializer_class = RestaurantSerializer


class FoodCategoryViewSet(viewsets.ModelViewSet):

    queryset = FoodCategory.objects.filter(
        is_active=True
    ).order_by('name')

    serializer_class = FoodCategorySerializer


class FoodItemViewSet(viewsets.ModelViewSet):

    queryset = FoodItem.objects.filter(
        is_available=True
    ).select_related(
        'restaurant',
        'category'
    )

    serializer_class = FoodItemSerializer


class CustomerViewSet(viewsets.ModelViewSet):

    queryset = Customer.objects.filter(
        is_active=True
    ).order_by('-created_at')

    serializer_class = CustomerSerializer


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all().prefetch_related(
        'items'
    ).order_by('-created_at')

    serializer_class = OrderSerializer

    def get_queryset(self):

        orders = super().get_queryset()

        now = timezone.now()

        for order in orders:

            elapsed = now - order.created_at

            new_status = order.status

            if elapsed < timedelta(minutes=1):

                new_status = 'PLACED'

            elif elapsed < timedelta(minutes=3):

                new_status = 'CONFIRMED'

            elif elapsed < timedelta(minutes=10):

                new_status = 'PREPARING'

            elif elapsed < timedelta(minutes=30):

                new_status = 'OUT_FOR_DELIVERY'

            else:

                new_status = 'DELIVERED'

            if order.status != new_status:

                order.status = new_status

                order.save(
                    update_fields=['status']
                )

        return orders