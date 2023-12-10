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

    readonly_fields = ('old_price', 'cartitem_old_price_total', 'single_price', 'total_price')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemsInline]

    # List display options for Cart
    list_display = ['member', 'total_products', 'prod_total_price', 'shipping_cost', 'SpecialDiscount', 'CouponDiscount', 'total_price', 'updated_at']
    search_fields = ['member__username', 'member__email']
    list_filter = ['created_at', 'updated_at']

    

    # Display the cart total price in the list
    readonly_fields = ('total_products', 'old_price', 'prod_total_price', 'total_discount', 'shipping_cost', 'total_disconts_after_snd', 'total_price' )


