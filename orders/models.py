from django.db import models
from members.models import Member  # Import the Members model
from products.models import Products  # Import the Products model

# Define the Order model
class Orders(models.Model):
    OrderID = models.AutoField(primary_key=True)
    Member = models.ForeignKey(Member, on_delete=models.CASCADE)
    OrderType = models.CharField(max_length=100)

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
    BuyerName = models.CharField(max_length=100)
    BuyerLastName = models.CharField(max_length=100)
    AddressType = models.CharField(max_length=100, choices=[('Invoice', 'Fatura'), ('Delivery', 'Teslimat')])
    City = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    FullAddress = models.CharField(max_length=100)
    PostalCode = models.IntegerField()
    PhoneNumber = models.IntegerField()
    EMail = models.EmailField()
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"OrderAddress {self.FullAddress} , {self.District}/{self.City}"

