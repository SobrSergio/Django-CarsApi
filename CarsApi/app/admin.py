from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'fuel_type', 'transmission', 'mileage', 'price')
    search_fields = ('brand', 'model', 'year', 'fuel_type', 'transmission')
    list_filter = ('brand', 'model', 'year', 'fuel_type', 'transmission')
