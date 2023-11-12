from django.contrib import admin
from .models import Cart, CartItems, CombinedProductChoice, ProductPrices

class CombinedProductChoiceInline(admin.TabularInline):
    model = CombinedProductChoice
    extra = 1
    fk_name = 'cart_item'



class CartItemsInline(admin.TabularInline):  # You can use StackedInline if you prefer that layout
    model = CartItems
    extra = 1

    def selected_combined_products(self, obj):
        if obj.is_combined_product:  # Check if the cart item is a combined product
            selected_products = CombinedProductChoice.objects.filter(cart_item=obj)
            return ', '.join([f'{product_combination.selected_product.product_name}' for product_combination in selected_products])
        else:
            return 'N/A'  # Return 'N/A' or similar if it's not a combined product
    selected_combined_products.short_description = 'Selected Combined Products'


    # Display the total price in the list
    readonly_fields = ('single_price', 'total_price', 'selected_combined_products')


@admin.register(CartItems)
class CartItemsAdmin(admin.ModelAdmin):
    inlines = [CombinedProductChoiceInline]


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemsInline]

    # List display options for Cart
    list_display = ['member', 'created_at', 'updated_at', 'total_products', 'total_price']
    search_fields = ['member__username', 'member__email']
    list_filter = ['created_at', 'updated_at']

    def total_products(self, obj):
        return sum(item.quantity for item in obj.user_cart.all())
    total_products.short_description = 'Toplam Ürün'

    # Display the cart total price in the list
    readonly_fields = ('total_products', 'total_price',)


