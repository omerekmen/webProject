from django.db import models
from datetime import datetime, timedelta

# Define the ProductCategory model
class ProductCategory(models.Model):
    ProductCategoryID = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=255)  # You can adjust the max length as needed

    def __str__(self):
        return f"{self.CategoryName}"

# Define the ProductCategorySizes model
class ProductCategorySizes(models.Model):
    CategorySizeID = models.AutoField(primary_key=True)
    ProductCategoryID = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    ProductSize = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.ProductSize}"


# Define the CombinationProduct model
class CombinationProduct(models.Model):
    CProductID = models.AutoField(primary_key=True)
    SProductInfo = models.JSONField(null=True, blank=True)
    CProductQuantity = models.IntegerField()

# Define the SetProduct model
class SetProduct(models.Model):
    SetID = models.AutoField(primary_key=True)
    SProductInfo = models.JSONField()
    SProductQuantity = models.IntegerField()

def upload_location(instance, filename):
    return f"product_files/{instance.products.product_name}/{filename}"

# Define the Products model
class Products(models.Model):
    PRODUCT_TYPE_CHOICES = [
        ('Set', 'Set'),
        ('Kombin', 'Kombin'),
        ('Tekil', 'Tekil'),
    ]

    ProductID = models.AutoField(primary_key=True)
    ProductCategoryID = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    product_type = models.CharField(
        max_length=100,
        choices=PRODUCT_TYPE_CHOICES,
        default='Tekil'  # You can set the default choice
    )    
    product_production_name = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_web_name = models.CharField(max_length=255)
    product_production_date = models.DateField()
    model_code = models.CharField(max_length=100)
    product_color = models.CharField(max_length=100) # CharField but we can create table of choices
    book_type = models.CharField(max_length=100, null=True, blank=True)    
    product_state = models.CharField(
        max_length=100,
        choices=[('Aktif', 'Aktif'), ('Pasif', 'Pasif'),],
        default='Aktif'  # You can set the default choice
    )
    product_genre = models.CharField(max_length=100,
                                    choices=[('Kız', 'Kız'), 
                                             ('Erkek', 'Erkek'),
                                             ('Unisex', 'Unisex'),])
    product_class = models.CharField(max_length=100, null=True, blank=True)
    product_level = models.CharField(max_length=100, null=True, blank=True)
    product_measure_unit = models.CharField(max_length=100)
    product_created_at = models.DateTimeField(auto_created=True)
    product_last_update = models.DateTimeField(auto_now=True)
    
    YEAR_CHOICES = [(r, r) for r in range(2000, datetime.today().year + 2)]
    season = models.IntegerField("Sezon", choices=YEAR_CHOICES, default=datetime.today().year)
    product_change_limit = models.JSONField(null=True, blank=True)

    def get_label_attr(self):
        today = datetime.now().date()
        days_ago = today - timedelta(days=30)
        return (self.product_created_at.date() > days_ago)

    # Define the label attribute
    label = property(get_label_attr)
    school_management = models.CharField(max_length=100)


    class Meta:
        ordering = ['-product_created_at']
        verbose_name = 'Ürünler'
        verbose_name_plural = 'Ürünler'

        permissions = [
            ("view_bk_products", "Can view bkAdmin products"),
            ("edit_bk_products", "Can edit bkAdmin products"),
            ("view_girne_products", "Can view girneAdmin products"),
            ("edit_girne_products", "Can edit girneAdmin products"),
        ]



    def __str__(self):
        return f"{self.product_name}"
    


# Define the ProductPrice model
class ProductPrices(models.Model):
    products = models.ForeignKey('Products', on_delete=models.CASCADE)

    SalePrice = models.DecimalField(max_digits=10, decimal_places=2)
    StrikedPrice = models.IntegerField(null=True, blank=True)

    DiscountRatio = models.IntegerField(null=True, blank=True)
    DiscountPrice = models.IntegerField(null=True, blank=True)
    DiscountType = models.IntegerField(null=True, blank=True)
    
    TaxPrice = models.CharField(max_length=100,
                                choices=[
                                    (0, '0%'),
                                    (10, '10%'),
                                    (20, '20%'),],
                                    null=True, blank=True)
    CombinePriceInfo = models.JSONField(null=True, blank=True)

    class Meta:
        verbose_name = 'Ürün Fiyat'
        verbose_name_plural = 'Ürün Fiyat'

    def save(self, *args, **kwargs):
        # Calculate DiscountRatio and DiscountPrice if StrikedPrice is provided
        if self.StrikedPrice:
            self.DiscountPrice = self.StrikedPrice - self.SalePrice
            if self.StrikedPrice > 0:
                self.DiscountRatio = (self.DiscountPrice / self.StrikedPrice) * 100
        else:
            # If StrikedPrice is not provided, set DiscountRatio and DiscountPrice to None
            self.DiscountPrice = None
            self.DiscountRatio = None

        super(ProductPrices, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.products} - {self.SalePrice}₺"


class ProductImages(models.Model):
    products = models.ForeignKey('Products', on_delete=models.CASCADE)
    product_image = models.FileField(upload_to=upload_location, null=True, blank=True)

    class Meta:
        verbose_name = 'Ürün Görselleri'
        verbose_name_plural = 'Ürün Görselleri'

class SizeBasedStocks(models.Model):
    products = models.ForeignKey('Products', on_delete=models.CASCADE)
    size = models.ForeignKey('ProductCategorySizes', on_delete=models.CASCADE)
    SKU_code = models.CharField(max_length=100)
    barcode = models.CharField(max_length=100)
    real_stock = models.IntegerField()
    sale_stock = models.IntegerField()
    reserved_stock = models.IntegerField()
    accept_stock = models.IntegerField()
    return_stock = models.IntegerField()
    cancel_stock = models.IntegerField()
    preproduction_stock = models.IntegerField()

    class Meta:
        verbose_name = 'Ürün Beden & Stok'
        verbose_name_plural = 'Ürün Beden & Stok'

    def __str__(self):
        return f"{self.products} - {self.size} - {self.sale_stock}"