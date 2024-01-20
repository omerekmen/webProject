from django.core.validators import MaxValueValidator
from django.utils import timezone
from django.db import models
from schools.models import *
from products.models import *
from members.models import Member


class SpecialDiscount(models.Model):
    sd_id = models.AutoField(primary_key=True)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE, verbose_name="Okul", related_name="special_discounts", help_text="Kampüs bazlı indirim uygulanacak okulu seçiniz.")
    campus = models.ManyToManyField(SchoolCampus, verbose_name="Kampüsler", related_name="special_discounts", blank=True, help_text="Kampüs bazlı indirim uygulanacak kampüsleri seçiniz.")
    member = models.ManyToManyField(Member, verbose_name="Öğrenciler", related_name="special_discounts", blank=True, help_text="Öğrenci bazlı indirim uygulanacak öğrencileri seçiniz. (Öğrencinin bulunduğu kampüs Kampüsler alanında seçilmişse bu alan boş bırakılabilir.)")
    products = models.ManyToManyField(Products, verbose_name="Ürünler", related_name="special_discounts", blank=True, help_text="Kampüs bazlı indirim uygulanacak ürünleri seçiniz. Boş bırakırsanız tüm ürünlerde indirim uygulanacaktır.")

    discountName = models.CharField(max_length=255, verbose_name="İndirim Adı")
    discountPerPerson = models.PositiveIntegerField(verbose_name="Kişi Başına İndirim Adedi", default=1, help_text="Kişi başına indirim adedi giriniz. Örnek: A kişisi bu indirimden 1 kere yararlanabilir.")
    discountAdminDescription = models.TextField(null=True, blank=True, verbose_name="Açıklama", help_text="İndirim açıklaması giriniz. Bu açıklamayı sadece adminler görecek.")
    discountDescription = models.TextField(null=True, blank=True, verbose_name="İndirim Açıklaması", help_text="İndirim açıklaması giriniz. Bu açıklamayı kullanı görecektir. Örnek: Seçili ürünlerde 2500₺ ve üzeri alışverişlerinize 10% (250₺) indirim fırsatı.")

    discountMinAmount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="İndirim Uygulanacak Minimum Tutar", default=0)
    discountType = models.CharField(max_length=255, verbose_name="İndirim Tipi", choices=(("percentage", "Yüzde"), ("amount", "Tutar")), default="percentage")
    discountAmount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="İndirim Tutarı", help_text="Yüzde için 0-100 arası değer giriniz.", default=0)

    cargoDiscount = models.BooleanField(verbose_name="Kargo İndirimi", default=False, help_text="Kargo indirimi uygulanacak mı?")
    cargoDiscountAmount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MaxValueValidator(100)], verbose_name="Kargo İndirim Oranı", default=0, help_text="Uygulanacak kargo indirimi oranını giriniz.",  null=True, blank=True)

    discountStartDate = models.DateTimeField(verbose_name="İndirim Başlangıç Tarihi", null=True, blank=True, help_text="İndirim başlangıç tarihi giriniz. Boş bırakırsanız indirim anında aktif olur.")
    discountEndDate = models.DateTimeField(verbose_name="İndirim Bitiş Tarihi", null=True, blank=True, help_text="İndirim bitiş tarihi giriniz. Boş bırakırsanız indirim süresiz devam eder.")
    discountStatus = models.BooleanField(verbose_name="İndirim Aktifliği", default=True, help_text="İndirim aktifliğini seçiniz. Bu alan seçtiğiniz tarih aralığına göre otomatik olarak güncellenecektir.")

    discountCreatedDate = models.DateTimeField(verbose_name="İndirim Oluşturulma Tarihi", auto_now_add=True)
    discountUpdatedDate = models.DateTimeField(verbose_name="İndirim Güncellenme Tarihi", auto_now=True)

    def save(self, *args, **kwargs):
        today = timezone.now()

        if self.discountStartDate and self.discountEndDate:
            self.discountStatus = self.discountStartDate <= today <= self.discountEndDate
        elif self.discountStartDate and not self.discountEndDate:
            self.discountStatus = self.discountStartDate <= today
        elif not self.discountStartDate and self.discountEndDate:
            self.discountStatus = today <= self.discountEndDate

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Özel İndirim"
        verbose_name_plural = "Özel İndirimler"

    def __str__(self):
        return f'{self.discountName}'

class DiscountCoupon(models.Model):
    dc_id = models.AutoField(primary_key=True)
    school = models.ForeignKey(Schools, on_delete=models.CASCADE, verbose_name="Okul", related_name="discount_coupon", help_text="Kampüs bazlı indirim uygulanacak okulu seçiniz.")
    campus = models.ManyToManyField(SchoolCampus, verbose_name="Kampüsler", related_name="discount_coupon", blank=True, help_text="Kampüs bazlı indirim uygulanacak kampüsleri seçiniz.")
    member = models.ManyToManyField(Member, verbose_name="Öğrenciler", related_name="discount_coupon", blank=True, help_text="Öğrenci bazlı indirim uygulanacak öğrencileri seçiniz. (Öğrencinin bulunduğu kampüs Kampüsler alanında seçilmişse bu alan boş bırakılabilir.)")

    discountName = models.CharField(max_length=255, verbose_name="İndirim Adı")
    discountCouponCode = models.CharField(max_length=255, verbose_name="İndirim Kupon Kodu", help_text="İndirim kupon kodunu giriniz.")
    discountPerPerson = models.PositiveIntegerField(verbose_name="Kişi Başı İndirim Hakkı", default=1, help_text="Kişi başına indirim adedi giriniz. Örnek: A kişisi bu indirimden 1 kere yararlanabilir.")
    discountTotalNumber = models.PositiveIntegerField(verbose_name="Toplam İndirim Adedi", default=1, help_text="Toplam indirim adedi giriniz. Örnek: Bu indirim kodu toplamda 100 kere kullanılabilir.")
    discountRemainingNumber = models.PositiveIntegerField(verbose_name="Kalan İndirim Adedi", default=1, help_text="Kalan indirim adedi. Bu alan otomatik hesaplanacaktır Örnek: Bu indirim kodu 100 kere kullanılabilir. 50 kere kullanıldı. Kalan indirim adedi 50'dir.")

    discountMinAmount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Minimum Sepet Tutarı", default=0, help_text="İndirim uygulanacak minimum sepet tutarını giriniz.")
    discountType = models.CharField(max_length=255, verbose_name="İndirim Tipi", choices=(("percentage", "Yüzde"), ("amount", "Tutar")), default="percentage")
    discountAmount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="İndirim Tutarı", help_text="Yüzde için 0-100 arası değer giriniz.", default=0)

    cargoDiscount = models.BooleanField(verbose_name="Kargo İndirimi", default=False, help_text="Kargo indirimi uygulanacak mı?")
    cargoDiscountAmount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MaxValueValidator(100)], verbose_name="Kargo İndirim Oranı", default=0, help_text="Uygulanacak kargo indirimi oranını giriniz.",  null=True, blank=True)

    discountStartDate = models.DateTimeField(verbose_name="İndirim Başlangıç Tarihi", null=True, blank=True, help_text="İndirim başlangıç tarihi giriniz. Boş bırakırsanız indirim anında aktif olur.")
    discountEndDate = models.DateTimeField(verbose_name="İndirim Bitiş Tarihi", null=True, blank=True, help_text="İndirim bitiş tarihi giriniz. Boş bırakırsanız indirim süresiz devam eder.")
    discountStatus = models.BooleanField(verbose_name="İndirim Aktifliği", default=True, help_text="İndirim aktifliğini seçiniz. Bu alan seçtiğiniz tarih aralığına göre otomatik olarak güncellenecektir.")
    discountAdminDescription = models.TextField(null=True, blank=True, verbose_name="Açıklama", help_text="İndirim açıklaması giriniz. Bu açıklamayı sadece adminler görecek.")

    discountCreatedDate = models.DateTimeField(verbose_name="İndirim Oluşturulma Tarihi", auto_now_add=True)
    discountUpdatedDate = models.DateTimeField(verbose_name="İndirim Güncellenme Tarihi", auto_now=True)

    def save(self, *args, **kwargs):
        today = timezone.now()

        if self.discountStartDate and self.discountEndDate:
            self.discountStatus = self.discountStartDate <= today <= self.discountEndDate
        elif self.discountStartDate and not self.discountEndDate:
            self.discountStatus = self.discountStartDate <= today
        elif not self.discountStartDate and self.discountEndDate:
            self.discountStatus = today <= self.discountEndDate

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "İndirim Kuponu"
        verbose_name_plural = "İndirim Kuponları"

    def __str__(self):
        return f'{self.discountName}'
    

class SpecialDiscountUsage(models.Model):
    sdu_id = models.AutoField(primary_key=True)
    discount = models.ForeignKey(SpecialDiscount, on_delete=models.CASCADE, verbose_name="Kullanılan İndirim")
    member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name="Kullanan Kişi")
    count_usage = models.PositiveIntegerField(default=0, verbose_name="Kullanım Sayısı")

    def __str__(self):
        return f'{self.member.first_name} {self.member.last_name}, {self.discount.discountName} indirimini {self.count_usage} kez kullandı.'

    class Meta:
        verbose_name = "Özel İndirim Kullanım"
        verbose_name_plural = "Özel İndirim Kullanımları"

class DiscountCouponUsage(models.Model):
    dcu_id = models.AutoField(primary_key=True)
    discount = models.ForeignKey(DiscountCoupon, on_delete=models.CASCADE, verbose_name="Kullanılan Kod")
    member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name="Kullanan Kişi")
    count_usage = models.PositiveIntegerField(default=0, verbose_name="Kullanım Sayısı")

    def __str__(self):
        return f'{self.member.first_name} {self.member.last_name}, {self.discount.discountCouponCode} kodunu {self.count_usage} kez kullandı.'

    class Meta:
        verbose_name = "Kupon Kullanım"
        verbose_name_plural = "Kupon Kullanımları"