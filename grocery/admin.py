from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import GroceryItem

@admin.register(GroceryItem)
class GroceryItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_kg')
