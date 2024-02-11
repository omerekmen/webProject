from django.db import models
from django.utils.translation import gettext_lazy as _
from members.models import Member
from coupons.models import *
from products.models import *
from school.models import *


# Define the Cart model
class Cart(models.Model):
    cart_id = models.BigAutoField(primary_key=True, unique=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="member_cart")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def shipping(self):
        return self.get_shipping_cost()
    
    @property
    def free_shipping_limit(self):
        return self.get_free_shipping_limit()
    
    @property
    def members_school(self):
        school = self.get_members_school()
        return school
    
    @property
    def members_campus(self):
        campus = SchoolCampus.objects.filter(member=self.member).first()
        return campus
    
    def get_members_school(self):
        school = Schools.objects.filter(schoolcampus__member=self.member).first()
        return school
    
    def get_shipping_cost(self):
        shipping_cost_obj = ShippingCost.objects.filter(school=self.get_members_school()).first()
        return shipping_cost_obj.shipping_cost if shipping_cost_obj else 0
    
    def get_free_shipping_limit(self):
        shipping_cost_obj = ShippingCost.objects.filter(school=self.get_members_school()).first()
        return shipping_cost_obj.free_shipping_limit if shipping_cost_obj else 0

    SpecialDiscountStatus = models.CharField(_('Özel İndirim'), max_length=100, choices=[('Özel İndirim Yok', 'Özel İndirim Yok'), ('Özel İndirim Uygulandı', 'Özel İndirim Uygulandı'), ('Admin İndirimi Uygulandı', 'Admin İndirimi Uygulandı'), ('Kampanya İndirimi', 'Kampanya İndirimi')], default="Özel İndirim Yok")
    SpecialDiscountApplied = models.ForeignKey(SpecialDiscount, on_delete=models.CASCADE, verbose_name='Uygulanan İndirim', null=True, blank=True)
    SpecialDiscount = models.DecimalField(_('Özel İndirim Tutarı'), max_digits=10, decimal_places=2, default=0)
    CouponCode = models.CharField(_('Uygulanan Kupon Kodu'), max_length=100, null=True, blank=True)
    CouponDiscount = models.DecimalField(_('Kupon İndirimi'), max_digits=10, decimal_places=2, default=0)


    class Meta:
        verbose_name = 'Sepet'
        verbose_name_plural = 'Sepetler'
        ordering = ['-created_at']


    ##### Ürün Striked Fiyatları Toplamı #####
    def old_price(self):
        total = 0
        for item in self.user_cart.all():
            product_price_obj = item.get_campus_based_price()
            if product_price_obj and product_price_obj.StrikedPrice is not None:
                total += product_price_obj.StrikedPrice * item.quantity
            else:
                total += item.single_price() * item.quantity
        return total
    
    ##### Satış Fiyatları Üzerinden Uygulanan İndirimler Toplamı #####
    def total_discount(self):
        total_discount = 0
        for item in self.user_cart.all():
            product_price_obj = item.get_campus_based_price()
            if product_price_obj and product_price_obj.DiscountPrice is not None:
                discount_per_item = product_price_obj.StrikedPrice - product_price_obj.SalePrice
                total_discount += discount_per_item * item.quantity
        return total_discount
    
    ##### Ürün Varsayılan Satış Fiyatları Toplamı #####
    def prod_total_price(self):
        total = sum(item.single_price() * item.quantity for item in self.user_cart.all())
        return total
    

    def total_products(self):
        return sum(item.quantity for item in self.user_cart.all())
    
    old_price.short_description = 'Toplam Ürün Fiyatı (İndirimsiz)'
    prod_total_price.short_description = 'SEPET ÜRÜN TOPLAMI'
    total_discount.short_description = 'Toplam Ürün İndirimleri'
    total_products.short_description = 'Toplam Ürün'

    def total_price_without_shipping(self):
        total = max(0, self.prod_total_price() - self.CouponDiscount - self.SpecialDiscount) 
        return total
    total_price_without_shipping.short_description = 'İndirimli Sepet Tutarı'

    ##### Shipping & Discount Coupon #####
    def shipping_cost(self):
        shipping_cost = self.shipping
        free_shipping_limit = self.free_shipping_limit
        if self.total_price_without_shipping() > free_shipping_limit:
            shipping_cost = 0
        if not self.user_cart.exists():  # assuming the related name is 'cartitems_set'
            shipping_cost = 0
        return shipping_cost
    
    def set_special_discount(self):
        special_discount = 0

        return special_discount
    
    def total_disconts_after_snd(self):
        total = self.total_discount()
        if self.shipping_cost() == 0 and not self.user_cart.exists:
            total += self.shipping
        if self.SpecialDiscount != 0:
            total += self.SpecialDiscount
        if self.CouponDiscount != 0:
            total += self.CouponDiscount
        return total
    
    def total_price(self):
        total = max(0, self.old_price() - self.total_discount() - self.CouponDiscount - self.SpecialDiscount) 
        total += self.shipping_cost()
        return total
    
    shipping_cost.short_description = 'Kargo Ücreti'
    total_disconts_after_snd.short_description = 'İNDİRİMLER TOPLAMI'
    total_price.short_description = 'SEPET TUTARI'



    def apply_special_discount(self):
        user_school = self.get_members_school()
        discount_man = DiscountManagement.objects.get(school=user_school)
        
        if not self.SpecialDiscountApplied:
            return

        if not discount_man.double_discount and discount_man.sd_priority == 'Düşük':
            self.SpecialDiscountStatus = 'Özel İndirim Yok'
            self.SpecialDiscountApplied = None
            self.SpecialDiscount = 0
            self.save()
            return
            
        special_products_total = 0
        for item in self.user_cart.all():
            if item.special_discount_applied():
                special_products_total += item.single_price() * item.quantity
                print(special_products_total)

        # Check if total meets the discount minimum amount
        if special_products_total >= self.SpecialDiscountApplied.discountMinAmount:
            if self.SpecialDiscountApplied.discountType == 'percentage':
                total_special_discount = special_products_total * self.SpecialDiscountApplied.discountAmount / 100
                print(total_special_discount)
            elif self.SpecialDiscountApplied.discountType == 'amount':
                total_special_discount = self.SpecialDiscountApplied.discountAmount
            else:
                total_special_discount = 0

            self.SpecialDiscount = total_special_discount
        else:
            self.SpecialDiscount = 0

        if self.SpecialDiscountApplied.cargoDiscount:
            print('Kargo İndirimi var')

        self.save()

    def special_discount(self):
        return self.SpecialDiscount
    
    special_discount.short_description = 'Özel İndirim'
    
    def total_after_special_discount(self):
        total_after_sd = self.prod_total_price() - self.SpecialDiscount
        return total_after_sd
    
    total_after_special_discount.short_description = "Özel İndirim Sonrası Sepet Tutarı"


    def apply_discount_coupon(self):
        member = self.member
        user_school = self.get_members_school()
        discount_man = DiscountManagement.objects.get(school=user_school)

        if not self.CouponCode:
            return 0

        if discount_man.double_discount == False and discount_man.dc_priority == 'Düşük':
            self.CouponCode = None
            self.CouponDiscount = 0
            self.save()
            return 0

        try:
            coupon = DiscountCoupon.objects.get(
                discountCouponCode=self.CouponCode,
                discountStatus=True,
                discountStartDate__lte=timezone.now(),
                discountEndDate__gte=timezone.now(),
            )

            if coupon.discountRemainingNumber != 0:
                if self.total_after_special_discount() >= coupon.discountMinAmount:
                    if coupon.discountType == 'percentage':
                        self.CouponDiscount = (self.total_after_special_discount() * coupon.discountAmount) / 100
                    elif coupon.discountType == 'amount':
                        self.CouponDiscount = coupon.discountAmount

                    coupon.discountRemainingNumber -= 1
                    coupon.save()
                else: 
                    self.CouponDiscount = 0

            else:
                self.CouponCode = None
                self.CouponDiscount = 0

        except DiscountCoupon.DoesNotExist:
            self.CouponCode = None
            self.CouponDiscount = 0

        # Save the updated cart
        self.save()

    def coupon_discount(self):
        return self.CouponDiscount
    
    coupon_discount.short_description = 'Kupon İndirimi'
    

    def __str__(self):
        return f'{self.member}'
    
    

# Define the CartItems model
class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='user_cart')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    size_stock = models.ForeignKey(SizeBasedStocks, on_delete=models.CASCADE, null=True, blank=True)
    is_combined_product = models.BooleanField(default=False)
    is_set_product = models.BooleanField(default=False)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_campus_based_price(self):
        # Assuming member has a 'campus' field
        campus_id = self.cart.member.campus_id
        prices = ProductPrices.objects.filter(products=self.product, campusPrice=campus_id)

        if prices.exists():
            return prices.first()
        else:
            # Fallback to general price if no campus-based price is found
            return ProductPrices.objects.filter(products=self.product).first()

    # Ürün Satış Fiyatı (Kampüs Bazında) 
    def single_price(self):
        product_price_obj = self.get_campus_based_price()
        if product_price_obj:
            sale_price = product_price_obj.SalePrice
            return sale_price
        return 0
    
    # Ürün Striked Fiyatı (Kampüs Bazında)
    def old_price(self):
        product_price_obj = self.get_campus_based_price()
        if product_price_obj and product_price_obj.StrikedPrice is not None:
            sale_price = product_price_obj.StrikedPrice
            return sale_price
        return 0
    
    def special_discount_applied(self):
        if not self.cart.SpecialDiscountApplied:
            return False

        special_discount = self.cart.SpecialDiscountApplied

        current_time = timezone.now()
        start_valid = special_discount.discountStartDate is None or special_discount.discountStartDate <= current_time
        end_valid = special_discount.discountEndDate is None or special_discount.discountEndDate >= current_time

        # Check if the special discount is active and within the valid date range
        if not (special_discount.discountStatus and start_valid and end_valid):
            return False

        # Check if special discount applies to all products (no specific products selected)
        if not special_discount.products.exists():
            return True

        # Check if this cart item's product is in the special discount's products
        return self.product in special_discount.products.all()
    
    special_discount_applied.short_description = "Özel İndirim Uygulandı"


    def cartitem_old_price_total(self):
        product_price_obj = self.get_campus_based_price()
        if product_price_obj and product_price_obj.StrikedPrice is not None:
            total = product_price_obj.StrikedPrice
            return total * self.quantity
        else:
            total = product_price_obj.SalePrice
            return total * self.quantity
        return 0
    
    def discount(self):
        # Retrieve the SalePrice from ProductPrices model
        product_price_obj = self.get_campus_based_price()
        if product_price_obj:
            sale_price = product_price_obj.DiscountPrice
            return sale_price * self.quantity
        return 0
    
    def total_price(self):
        # Retrieve the SalePrice from ProductPrices model
        product_price_obj = self.get_campus_based_price()
        if product_price_obj:
            sale_price = product_price_obj.SalePrice
            return sale_price * self.quantity
        return 0
    
    single_price.short_description = 'SATIŞ FİYATI'
    old_price.short_description = 'Eski Fiyat'
    discount.short_description = 'İndirim'
    cartitem_old_price_total.short_description = 'Eski Toplam Fiyat'
    total_price.short_description = 'ÜRÜN SEPET TUTARI'

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