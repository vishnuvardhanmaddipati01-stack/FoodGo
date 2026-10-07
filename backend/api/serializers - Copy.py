from django.db import transaction
from rest_framework import serializers

from .models import (
    Restaurant,
    FoodCategory,
    FoodItem,
    Customer,
    Order,
    OrderItem
)


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = [
            'id',
            'name',
            'description',
            'address',
            'rating',
            'image',
            'is_active',
            'created_at',
        ]


class FoodCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = FoodCategory
        fields = [
            'id',
            'name',
            'image',
            'is_active',
        ]


class FoodItemSerializer(serializers.ModelSerializer):

    restaurant_name = serializers.CharField(
        source='restaurant.name',
        read_only=True
    )

    category_name = serializers.CharField(
        source='category.name',
        read_only=True
    )

    class Meta:
        model = FoodItem

        fields = [
            'id',
            'restaurant',
            'restaurant_name',
            'category',
            'category_name',
            'name',
            'description',
            'price',
            'image',
            'is_vegetarian',
            'is_available',
            'created_at',
        ]


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer

        fields = [
            'id',
            'mobile',
            'name',
            'email',
            'address',
            'is_active',
            'created_at',
        ]

        read_only_fields = [
            'id',
            'created_at',
        ]


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem

        fields = [
            'id',
            'food',
            'food_name',
            'price',
            'quantity',
            'item_total',
        ]

        read_only_fields = [
            'id',
            'food_name',
            'price',
            'item_total',
        ]


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(
        many=True,
        write_only=True
    )

    order_items = OrderItemSerializer(
        source='items',
        many=True,
        read_only=True
    )

    class Meta:
        model = Order

        fields = [
            'id',
            'customer',
            'customer_name',
            'mobile',
            'address',
            'payment_method',
            'total_amount',
            'status',
            'created_at',
            'items',
            'order_items',
        ]

        read_only_fields = [
            'id',
            'total_amount',
            'status',
            'created_at',
            'order_items',
        ]

    @transaction.atomic
    def create(self, validated_data):

        items_data = validated_data.pop(
            'items'
        )

        total_amount = 0

        order = Order.objects.create(
            total_amount=0,
            **validated_data
        )

        for item_data in items_data:

            food = item_data['food']

            quantity = item_data['quantity']

            price = food.price

            item_total = price * quantity

            total_amount += item_total

            OrderItem.objects.create(
                order=order,
                food=food,
                food_name=food.name,
                price=price,
                quantity=quantity,
                item_total=item_total
            )

        order.total_amount = total_amount

        order.save()

        return order