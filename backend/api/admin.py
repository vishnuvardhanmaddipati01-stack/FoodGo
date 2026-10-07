from django.contrib import admin

from .models import (
    Restaurant,
    FoodCategory,
    FoodItem,
    Customer
)


admin.site.register(Restaurant)
admin.site.register(FoodCategory)
admin.site.register(FoodItem)
admin.site.register(Customer)