from django.db import models
from products.models import Products
from members.models import Member


# Define the Cart model
class Cart(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Sepet'
        verbose_name_plural = 'Sepetler'
        ordering = ['-created_at']

    # def __str__(self):
    #     return f"{self.cart_id} - {self.member} - {self.product} - {self.quantity} - {self.created_at} - {self.updated_at}"

    def total_price(self):
        return self.quantity * self.product.product_price
    

# Define the CartItems model
class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Sepet Ürün'
        verbose_name_plural = 'Sepet Ürünler'
        ordering = ['-created_at']

    # def __str__(self):
    #     return f"{self.cart_item_id} - {self.cart} - {self.product} - {self.quantity} - {self.created_at} - {self.updated_at}"

    def total_price(self):
        return self.quantity * self.product.product_price