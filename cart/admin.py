from .models import Cart, CartItems, CombinedProductChoice, ProductPrices
from django.utils.safestring import mark_safe
from django.contrib import admin

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
            sp = '<br>'.join([f'{product_combination.selected_product.product_name} ({product_combination.size_stock.size})' for product_combination in selected_products])
            return mark_safe(sp)
        else:
            return 'N/A'  # Return 'N/A' or similar if it's not a combined product
    selected_combined_products.short_description = 'Selected Combined Products'


    # Display the total price in the list
    readonly_fields = ('single_price', 'total_price', 'selected_combined_products', 'special_discount_applied')


@admin.register(CartItems)
class CartItemsAdmin(admin.ModelAdmin):
    inlines = [CombinedProductChoiceInline]

    readonly_fields = ('old_price', 'cartitem_old_price_total', 'single_price', 'total_price', 'special_discount_applied')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemsInline]

    # List display options for Cart
    list_display = ['member', 'total_products', 'prod_total_price', 'shipping_cost', 'SpecialDiscount', 'CouponDiscount', 'total_price', 'updated_at']
    search_fields = ['member__username', 'member__email']
    list_filter = ['created_at', 'updated_at']

    

    # Display the cart total price in the list
    readonly_fields = ('total_products', 'old_price', 'total_discount', 'prod_total_price', 'special_discount', 'total_after_special_discount', 'coupon_discount', 'total_disconts_after_snd', 'shipping_cost', 'total_price' )

