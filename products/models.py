from django.db import models



# Define the ProductCategory model
class ProductCategory(models.Model):
    ProductCategoryID = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=255)  # You can adjust the max length as needed

# Define the ProductCategorySizes model
class ProductCategorySizes(models.Model):
    CategorySizeID = models.AutoField(primary_key=True)
    ProductCategoryID = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    ProductSize = models.CharField(max_length=100)

# Define the ProductStock model
class ProductStock(models.Model):
    StockID = models.AutoField(primary_key=True)
    RealStock = models.IntegerField()
    SaleStock = models.IntegerField()
    ReservedStock = models.IntegerField()
    AcceptStock = models.IntegerField()
    ReturnStock = models.IntegerField()
    CancelStock = models.IntegerField()
    PreproductionStock = models.IntegerField()

# Define the ProductPrice model
class ProductPrice(models.Model):
    PriceID = models.AutoField(primary_key=True)
    SalePrice = models.DecimalField(max_digits=10, decimal_places=2)
    StrikedPrice = models.IntegerField()
    DiscountRatio = models.IntegerField()
    DiscountPrice = models.IntegerField()
    DiscountType = models.CharField(max_length=100)
    TaxPrice = models.CharField(max_length=100)
    CombinePriceInfo = models.JSONField()

# Define the CombinationProduct model
class CombinationProduct(models.Model):
    CProductID = models.AutoField(primary_key=True)
    SProductInfo = models.JSONField()
    CProductQuantity = models.IntegerField()

# Define the SetProduct model
class SetProduct(models.Model):
    SetID = models.AutoField(primary_key=True)
    SProductInfo = models.JSONField()
    SProductQuantity = models.IntegerField()

# Define the Products model
class Products(models.Model):
    ProductID = models.AutoField(primary_key=True)
    ProductCategoryID = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    CategorySizeID = models.ForeignKey(ProductCategorySizes, on_delete=models.CASCADE)
    product_type = models.CharField(max_length=100)
    product_production_name = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_web_name = models.CharField(max_length=255)
    product_production_date = models.DateField()
    SKU_code = models.CharField(max_length=100)
    barcode = models.CharField(max_length=100)
    model_code = models.CharField(max_length=100)
    StockID = models.ForeignKey(ProductStock, on_delete=models.CASCADE)
    PriceID = models.ForeignKey(ProductPrice, on_delete=models.CASCADE)
    product_color = models.CharField(max_length=100)
    book_type = models.CharField(max_length=100)
    product_state = models.IntegerField()
    product_genre = models.CharField(max_length=100)
    product_class = models.CharField(max_length=100)
    product_level = models.CharField(max_length=100)
    product_image = models.URLField()
    product_measure_unit = models.CharField(max_length=100)
    product_created_at = models.DateTimeField()
    product_last_update = models.DateTimeField()
    product_season = models.DateField()
    product_change_limit = models.JSONField()

    def __str__(self):
        return f"{self.product_name}"
