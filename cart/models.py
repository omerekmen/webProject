from django.db import models
from products.models import Products, CombinationProduct, ProductPrices, SizeBasedStocks
from members.models import Member


# Define the Cart model
class Cart(models.Model):
    cart_id = models.BigAutoField(primary_key=True, unique=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Sepet'
        verbose_name_plural = 'Sepetler'
        ordering = ['-created_at']

    # def __str__(self):
    #     return f"{self.cart_id} - {self.member} - {self.product} - {self.quantity} - {self.created_at} - {self.updated_at}"

    def total_price(self):
        total = 0
        cart_items = CartItems.objects.filter(cart=self)

        for item in cart_items:
            product_price_obj = ProductPrices.objects.filter(products=item.product).first()
            if product_price_obj:
                total += product_price_obj.SalePrice * item.quantity

        return total
    
    def old_price(self):
        total = 0
        cart_items = CartItems.objects.filter(cart=self)

        for item in cart_items:
            product_price_obj = ProductPrices.objects.filter(products=item.product).first()
            if product_price_obj:
                if product_price_obj.DiscountPrice is not None:
                    total += product_price_obj.StrikedPrice * item.quantity
                else:
                    total += product_price_obj.SalePrice * item.quantity

        return total
    
    def total_discount(self):
        total = 0
        cart_items = CartItems.objects.filter(cart=self)

        for item in cart_items:
            product_price_obj = ProductPrices.objects.filter(products=item.product).first()
            if product_price_obj and product_price_obj.DiscountPrice is not None:
                total += product_price_obj.DiscountPrice * item.quantity
            else:
                total += 0

        return total
    
    def total_products(self):
        return sum(item.quantity for item in self.user_cart.all())
    total_products.short_description = 'Toplam Ürün'
    
    total_price.short_description = 'Toplam Fiyat'

    def __str__(self):
        return f'{self.member}'
    
    

# Define the CartItems model
class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='user_cart')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    size_stock = models.ForeignKey(SizeBasedStocks, on_delete=models.CASCADE, null=True, blank=True)
    is_combined_product = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def single_price(self):
        # Retrieve the SalePrice from ProductPrices model
        product_price_obj = ProductPrices.objects.filter(products=self.product).first()
        if product_price_obj:
            sale_price = product_price_obj.SalePrice
            return sale_price
        return 0
    
    def old_price(self):
        # Retrieve the SalePrice from ProductPrices model
        product_price_obj = ProductPrices.objects.filter(products=self.product).first()
        if product_price_obj and product_price_obj.StrikedPrice is not None:
            sale_price = product_price_obj.StrikedPrice
            return sale_price
        return 0

    def cartitem_total(self):
        product_price_obj = ProductPrices.objects.filter(products=self.product).first()
        if product_price_obj and product_price_obj.StrikedPrice is not None:
            total = product_price_obj.StrikedPrice
            return total * self.quantity
        else:
            total = product_price_obj.SalePrice
            return total * self.quantity
        return 0
    
    def discount(self):
        # Retrieve the SalePrice from ProductPrices model
        product_price_obj = ProductPrices.objects.filter(products=self.product).first()
        if product_price_obj:
            sale_price = product_price_obj.DiscountPrice
            return sale_price * self.quantity
        return 0
    
    single_price.short_description = 'Tekil Fiyat'
    old_price.short_description = 'Eski Fiyat'
    discount.short_description = 'İndirim'

    def total_price(self):
        # Retrieve the SalePrice from ProductPrices model
        product_price_obj = ProductPrices.objects.filter(products=self.product).first()
        if product_price_obj:
            sale_price = product_price_obj.SalePrice
            return sale_price * self.quantity
        return 0
    
    total_price.short_description = 'Toplam Fiyat'

    class Meta:
        verbose_name = 'Sepet Ürün'
        verbose_name_plural = 'Sepet Ürünler'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.cart} / {self.product}'
    

class CombinedProductChoice(models.Model):
    cart_item = models.ForeignKey(CartItems, on_delete=models.CASCADE)
    combination_product_category = models.ForeignKey(CombinationProduct, on_delete=models.CASCADE)
    selected_product = models.ForeignKey(Products, on_delete=models.CASCADE)
    size_stock = models.ForeignKey(SizeBasedStocks, on_delete=models.CASCADE, null=True, blank=True)
