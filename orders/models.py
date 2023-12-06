from django.db import models
from members.models import Member  # Import the Members model
from products.models import Products  # Import the Products model
from store.models import *  # Import the Products model
from django.utils.translation import gettext_lazy as _
import random


# Define the Order model
class Orders(models.Model):
    OrderID = models.SlugField(primary_key=True, editable=False, unique=True, max_length=10)
    Member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='TC No')
    OrderType = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.OrderID:
            # Generate a unique Order ID
            self.OrderID = self.generate_unique_order_id()
        super(Orders, self).save(*args, **kwargs)

    @staticmethod
    def generate_unique_order_id():
        range_start = 10**(6-1)
        range_end = (10**10)-1
        order_id = str(random.randint(range_start, range_end))

        while Orders.objects.filter(OrderID=order_id).exists():
            order_id = str(random.randint(range_start, range_end))
        return order_id
    
    def memberName(self):
        if self.Member:
            return f"{self.Member.first_name} {self.Member.last_name}"
        return None
    def memberCampus(self):
        if self.Member:
            return f"{self.Member.campus_id.campus_name}"
        return None
    
    memberName.short_description = 'Öğrenci Bilgileri'
    memberCampus.short_description = 'Öğrenci Şube'
    

    InvoiceInfoID = models.IntegerField()
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    OrderStatus = models.CharField(max_length=100)
    OrderProductQuantity = models.IntegerField()
    OrderTaxAmount = models.IntegerField()
    TotalDiscountAmount = models.IntegerField()
    OrderCargoFee = models.IntegerField()
    GiftAmount = models.DecimalField(max_digits=10, decimal_places=2)
    SpecialDiscount = models.DecimalField(max_digits=10, decimal_places=2)
    PaymentInfoID = models.IntegerField()

    WarehouseID = models.IntegerField()
    WarehouseStatus = models.CharField(max_length=100)
    CargoStatus = models.CharField(max_length=100)
    CargoTrackNumber = models.IntegerField()
    EstimatedDeliveryDate = models.DateField()
    ActualDeliveryDate = models.DateField()
    DeliveryInfoID = models.IntegerField()
    
    ExternalReferenceID = models.IntegerField()

    OrderDate = models.DateTimeField(auto_now_add=True)
    LastUpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.OrderID}"

# Define the OrderProducts model
class OrderProducts(models.Model):
    Order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Products, on_delete=models.CASCADE)
    ProductType = models.CharField(max_length=100) # Bence Gereksiz çünkü ProductID ile zaten ilişkili
    Quantity = models.IntegerField(default=1)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def subtotal(self):
        return self.Quantity * self.ProductID.ProductPrices.SalePrice

    def __str__(self):
        return f"{self.ProductID.product_name} - {self.Quantity} (pieces) - {self.subtotal()}"

class OrderAddress(models.Model):
    Order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    AddressType = models.CharField(max_length=100, choices=[('Delivery', 'Teslimat'), ('Invoice', 'Fatura')])

    recipient_name = models.CharField(max_length=255)
    recipient_lastname = models.CharField(max_length=255)

    Country = models.CharField(max_length=100, default="Türkiye")
    City = models.ForeignKey(City, on_delete=models.CASCADE)
    District = models.ForeignKey(District, on_delete=models.CASCADE)
    FullAddress = models.TextField()
    PostalCode = models.PositiveIntegerField(null=True, blank=True)

    PhoneNumber = models.IntegerField()
    EMail = models.EmailField()

    comp_name = models.CharField(max_length=255, null=True, blank=True)
    tax_office = models.CharField(max_length=255, null=True, blank=True)
    tax_no = models.PositiveBigIntegerField(null=True, blank=True)

    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"""{self.recipient_name} {self.recipient_lastname}
            {self.PhoneNumber} / {self.EMail}
            {self.FullAddress} , {self.District}/{self.City}"""