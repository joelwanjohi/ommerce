from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    # Fields to display in the product list page in the admin panel
    list_display = ('id', 'name', 'price', 'category', 'quantity', 'unit_price', 'location')
    
    # Add search functionality for the product name, category, and description
    search_fields = ('name', 'category', 'description')
    
    # Add filters to help filter by category
    list_filter = ('category',)
    
    # Add fields to the form in the admin page for easier editing
    fields = ('owner', 'name', 'category', 'quantity', 'description', 'image', 'price', 'location', 'unit_price')
    
    # Make the price field editable only if the unit_price is not set
    def save_model(self, request, obj, form, change):
        if not obj.unit_price:
            obj.unit_price = obj.price * obj.quantity
        super().save_model(request, obj, form, change)

# Register the Product model with the custom admin class
admin.site.register(Product, ProductAdmin)
