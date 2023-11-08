from django.db import models
from schools.models import Schools
from ckeditor.fields import RichTextField
from datetime import datetime, timedelta
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _


##########################################################################################
#################################       CATEGORIES     ###################################
##########################################################################################


class ProductCategory(models.Model):
    ProductCategoryID = models.AutoField(primary_key=True)
    CategoryName = models.CharField(_('Kategori Adı'), max_length=255)  # You can adjust the max length as needed

    def get_subcategories(self):
        subcategories = ProductSubCategory.objects.filter(ProductCategory=self.ProductCategoryID)
        return ", ".join([subcategory.SubCategoryName for subcategory in subcategories])
    
    get_subcategories.short_description = 'Alt Kategoriler'

    class Meta:
        verbose_name = 'Ürün Kategorileri'
        verbose_name_plural = 'Ürün Kategorileri'

    def __str__(self):
        return f"{self.CategoryName}"

class ProductSubCategory(models.Model):
    ProductSubCategoryID = models.AutoField(primary_key=True)
    ProductCategory = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    SubCategoryName = models.CharField(max_length=255)  # You can adjust the max length as needed

    def get_category_name(self):
       category_name = self.ProductCategory.CategoryName
       return category_name
    
    get_category_name.short_description = 'Kategori Adı'

    class Meta:
        verbose_name = 'Ürün Alt Kategorileri'
        verbose_name_plural = 'Ürün Alt Kategorileri'

    def __str__(self):
        return f"{self.ProductCategory.CategoryName} / {self.SubCategoryName}"


##########################################################################################
#################################         SİZE         ###################################
##########################################################################################

class ProductCategorySizes(models.Model):
    CategorySizeID = models.AutoField(primary_key=True)
    ProductSize = models.CharField(max_length=100)

    class Meta:
        ordering = ['CategorySizeID']
        verbose_name = 'Ürün Bedenleri'
        verbose_name_plural = 'Ürün Bedenleri'

    def __str__(self):
        return f"{self.ProductSize}"



##########################################################################################
#################################        PRODUCTS      ###################################
##########################################################################################


def upload_location(instance, filename):
    return f"product_files/{instance.products.product_name}/{filename}"

class Products(models.Model):
    PRODUCT_TYPE_CHOICES = [('Set', 'Set'), ('Kombin', 'Kombin'), ('Tekil', 'Tekil'),]

    ProductID = models.AutoField(_('Ürün ID'), primary_key=True)
    ProductSubCategoryID = models.ForeignKey(ProductSubCategory, on_delete=models.CASCADE, related_name='product_subcategory')
    product_type = models.CharField(_('Ürün Türü'), 
        max_length=100,
        choices=PRODUCT_TYPE_CHOICES,
        default='Tekil'  
    )    
    product_production_name = models.CharField(_('Ürün Üretim Adı'), max_length=255)
    product_name = models.CharField(_('Ürün Adı'), max_length=255)
    product_web_name = models.CharField(_('Ürün Web Adı'), max_length=255)
    product_production_date = models.DateField(_('Üretim Tarihi'), )
    model_code = models.CharField(_('Model Kodu'), max_length=100)
    product_color = models.CharField(_('Ürün Rengi'), max_length=100) # CharField but we can create table of choices
    book_type = models.CharField(max_length=100, null=True, blank=True)    
    product_state = models.CharField(_('Ürün Durumu'), 
        max_length=100,
        choices=[('Aktif', 'Aktif'), ('Pasif', 'Pasif'),],
        default='Aktif' 
    )
    product_genre = models.CharField(_('Cinsiyet'), max_length=100,
                                    choices=[('Kız', 'Kız'), 
                                             ('Erkek', 'Erkek'),
                                             ('Unisex', 'Unisex'),])
    product_class = models.CharField(max_length=100, null=True, blank=True)
    product_level = models.CharField(max_length=100, null=True, blank=True)
    product_measure_unit = models.CharField(max_length=100)
    product_created_at = models.DateTimeField(_('Oluşturulma Tarihi'), auto_now_add=True)
    product_last_update = models.DateTimeField(_('Güncelleme Tarihi'), auto_now=True)
    
    YEAR_CHOICES = [(r, r) for r in range(2000, datetime.today().year + 2)]
    season = models.IntegerField("Sezon", choices=YEAR_CHOICES, default=datetime.today().year)
    product_change_limit = models.JSONField(null=True, blank=True)

    def get_label_attr(self):
        today = datetime.now().date()
        days_ago = today - timedelta(days=30)
        return (self.product_created_at.date() > days_ago)

    label = property(get_label_attr)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE, default=1)

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

    def product_image(self):
        # Get the first image for the product
        product_image = ProductImages.objects.filter(products=self).first()
        if product_image:
            return mark_safe(f'<img src="{product_image.product_image.url}" width="100" height="100" />')
        return None
    
    product_image.short_description = 'Ürün Resmi'


    def __str__(self):
        return f"{self.product_name}"
    


##########################################################################################
##########################     COMBINATION AND SET PRODUCTS     ##########################
##########################################################################################


class CombinationProduct(models.Model):
    Product = models.ForeignKey('Products', on_delete=models.CASCADE)
    CProductCategory = models.CharField(max_length=100)
    CombinProducts = models.ManyToManyField('Products', related_name='combin_products', verbose_name='Ürün Seçimi', blank=True)

class SetProduct(models.Model):
    SetID = models.AutoField(primary_key=True)
    SProductInfo = models.JSONField()
    SProductQuantity = models.IntegerField()


##########################################################################################
########################       PRODUCT ATTRIBUTES         ################################
##########################################################################################


class ProductPrices(models.Model):
    products = models.ForeignKey('Products', on_delete=models.CASCADE)

    SalePrice = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    StrikedPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

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
    real_stock = models.PositiveIntegerField(default=0)
    sale_stock = models.PositiveIntegerField(default=0)
    reserved_stock = models.PositiveIntegerField(default=0)
    accept_stock = models.PositiveIntegerField(default=0)
    return_stock = models.PositiveIntegerField(default=0)
    cancel_stock = models.PositiveIntegerField(default=0)
    preproduction_stock = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Ürün Beden & Stok'
        verbose_name_plural = 'Ürün Beden & Stok'

    def __str__(self):
        return f"{self.products} - {self.size} - {self.sale_stock}"


class ProductDetails(models.Model):
    products = models.ForeignKey('Products', on_delete=models.CASCADE)
    product_short_desc = RichTextField(null=True, blank=True)
    product_detail = RichTextField(_('Ürün Bilgileri'), null=True, blank=True)
    product_info = RichTextField(null=True, blank=True)
    product_size_table = RichTextField(null=True, blank=True)
    product_suggestions = RichTextField(null=True, blank=True)
    product_quality = RichTextField(null=True, blank=True)
    product_find_size = RichTextField(null=True, blank=True)
    product_measure = RichTextField(null=True, blank=True)
    product_video = RichTextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Ürün Detayları'
        verbose_name_plural = 'Ürün Detayları'

    def __str__(self):
        return f"{self.products} - {self.product_detail}"