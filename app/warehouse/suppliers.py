from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, verbose_name="Üretici Adı")
    address = models.CharField(max_length=200, verbose_name="Adres")
    tax_no = models.CharField(max_length=20, verbose_name="Vergi No", blank=True, null=True)
    email = models.EmailField(max_length=50, verbose_name="E-posta", blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name="Telefon", blank=True, null=True)
    fax = models.CharField(max_length=20, verbose_name="Faks", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Üretici"
        verbose_name_plural = "Üreticiler"

class Supplier(models.Model):
    name = models.CharField(max_length=50, verbose_name="Tedarikçi Adı")
    address = models.CharField(max_length=200, verbose_name="Adres")
    tax_no = models.CharField(max_length=20, verbose_name="Vergi No", blank=True, null=True)
    email = models.EmailField(max_length=50, verbose_name="E-posta", blank=True, null=True)
    phone = models.CharField(max_length=20, verbose_name="Telefon", blank=True, null=True)
    fax = models.CharField(max_length=20, verbose_name="Faks", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Tedarikçi"
        verbose_name_plural = "Tedarikçiler"


class Shipment(models.Model):
    name = models.CharField(max_length=50, verbose_name="Sevkiyat Adı")
    vehicle_type = models.CharField(max_length=50, choices=[('Tır', 'Tır'), ('Kamyon', 'Kamyon'), ('Kargo', 'Kargo'),], verbose_name="Araç Tipi")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, verbose_name="Üretici", blank=True, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name="Tedarikçi", blank=True, null=True)
    warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE, verbose_name="Depo")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Sevkiyat"
        verbose_name_plural = "Sevkiyatlar"


class Waybill(models.Model):
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE, verbose_name="Sevkiyat")
    waybill_no = models.CharField(max_length=50, verbose_name="İrsaliye No")
    waybill_date = models.DateField(verbose_name="İrsaliye Tarihi")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Güncellenme Tarihi")

    def __str__(self):
        return f'{self.waybill_no}'

    class Meta:
        verbose_name = "İrsaliye"
        verbose_name_plural = "İrsaliyeler"

class WaybillProduct(models.Model):
    waybill = models.ForeignKey(Waybill, on_delete=models.CASCADE, verbose_name="İrsaliye")
    product = models.ForeignKey('products.Products', on_delete=models.CASCADE, verbose_name="Ürün")
    product_size = models.ForeignKey('products.ProductCategorySizes', on_delete=models.CASCADE, verbose_name="Ürün Boyutu")
    quantity = models.PositiveIntegerField(verbose_name="Beklenen Miktar")
    act_quantity = models.PositiveIntegerField(verbose_name="Sayılan Miktar", blank=True, null=True)

    def stockControl(self):
        if self.act_quantity is None:
            return "Henüz Stok Sayımı Yapılmadı"

        if self.quantity == self.act_quantity:
            return "Stok Doğrulandı"
        else:
            if self.quantity > self.act_quantity:
                return f"{self.quantity - self.act_quantity} Adet Eksik"
            else:
                return f"{self.act_quantity - self.quantity} Adet Fazla"

    def __str__(self):
        return f'{self.waybill} - {self.product}'

    class Meta:
        verbose_name = "İrsaliye Ürün"
        verbose_name_plural = "İrsaliye Ürünler"

# class WaybillControl(models.Model):
#     waybill = models.ForeignKey(Waybill, on_delete=models.CASCADE, verbose_name="İrsaliye")
#     warehouse = models.ForeignKey('Warehouse', on_delete=models.CASCADE, verbose_name="Depo")
#     product = models.ForeignKey('products.Products', on_delete=models.CASCADE, verbose_name="Ürün")
#     product_size = models.ForeignKey('products.ProductCategorySizes', on_delete=models.CASCADE, verbose_name="Ürün Boyutu")
#     quantity = models.PositiveIntegerField(verbose_name="Miktar")

#     def __str__(self):
#         return f'{self.waybill} - {self.product}'

    class Meta:
        verbose_name = "İrsaliye Kontrol"
        verbose_name_plural = "İrsaliye Kontrolleri"