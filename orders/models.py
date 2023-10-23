from django.db import models
from members.models import Members  # Import the Members model
from products.models import Products  # Import the Products model

# Define the Order model
class Orders(models.Model):
    OrderID = models.AutoField(primary_key=True)
    MemberID = models.ForeignKey(Members, on_delete=models.CASCADE)
    OrderStatus = models.CharField(max_length=100)
    CargoStatus = models.CharField(max_length=100)
    WarehouseStatus = models.CharField(max_length=100)
    OrderDate = models.DateField()
    LastUpdatedAt = models.DateField()
    EstimatedDeliveryDate = models.DateField()
    ActualDeliveryDate = models.DateField()
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    OrderProductQuantity = models.IntegerField()
    OrderTaxAmount = models.IntegerField()
    TotalDiscountAmount = models.IntegerField()
    OrderCargoFee = models.IntegerField()
    GiftAmount = models.DecimalField(max_digits=10, decimal_places=2)
    SpecialDiscount = models.DecimalField(max_digits=10, decimal_places=2)
    PaymentInfoID = models.IntegerField()
    DeliveryInfoID = models.IntegerField()
    ExternalReferenceID = models.IntegerField()
    InvoiceInfoID = models.IntegerField()
    CargoTrackNumber = models.IntegerField()
    OrderType = models.CharField(max_length=100)
    WarehouseID = models.IntegerField()

    def __str__(self):
        return f"Order {self.OrderID}"

# Define the OrderProducts model
class OrderProducts(models.Model):
    OrderProductID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Products, on_delete=models.CASCADE)
    ProductType = models.CharField(max_length=100)
    Quantity = models.IntegerField()
    SubTotal = models.DecimalField(max_digits=10, decimal_places=2)
    CreatedAt = models.DateTimeField()
    UpdatedAt = models.DateTimeField()

    def __str__(self):
        return f"OrderProduct {self.OrderProductID}"
