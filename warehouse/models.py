from django.db import models


class Warehouse(models.Model):
    name = models.CharField(max_length=50, verbose_name="Depo Adı")
    address = models.CharField(max_length=200, verbose_name="Adres")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    fax = models.CharField(max_length=20, verbose_name="Faks")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Depo"
        verbose_name_plural = "Depolar"


class WarehouseStock(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, verbose_name="Depo")
    product = models.ForeignKey('products.Products', on_delete=models.CASCADE, verbose_name="Ürün")
    product_size = models.ForeignKey('products.ProductCategorySizes', on_delete=models.CASCADE, verbose_name="Ürün Boyutu", blank=True, null=True)
    stock = models.PositiveIntegerField(verbose_name="Stok")

    def __str__(self):
        return f'{self.warehouse} - {self.product}'

    class Meta:
        verbose_name = "Depo Stok"
        verbose_name_plural = "Depo Stokları"
        unique_together = ['warehouse', 'product']