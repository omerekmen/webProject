from django.db import models
from members.models import Member
import random, datetime

class SupportTicket(models.Model):
    TICKET_STATUS_CHOICES = [
        ('OPEN', 'Aktif'),
        ('IN_PROGRESS', 'Talebiniz İnceleniyor'),
        ('CLOSED', 'Çözüldü'),
    ]

    ticket_id = models.SlugField(primary_key=True, editable=False, unique=True, max_length=10, verbose_name='Destek No')
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=[('Kıyafet', 'Kıyafet'), ('Kitap', 'Kitap')])
    subject = models.CharField(max_length=200, choices = [
    ('Degisim', 'Kıyafet/Değişim'), 
    ('Iade', 'Kıyafet/İade'), 
    ('Iptal', 'Kıyafet/İptal'), 
    ('Fatura', 'Kıyafet/Fatura'), 
    ('Urun', 'Kıyafet/Ürün'), 
    ('Siparis', 'Kıyafet/Sipariş'), 
    ('Web', 'Kıyafet/Web'), 
    ('Kargo', 'Kıyafet/Kargo'), 
    ('Teslimat', 'Kıyafet/Teslimat'), 
    ('Odeme', 'Kıyafet/Ödeme'), 
    ('HataliUrun', 'Kıyafet/Hatalı Ürün'), 
    ('EskiUrun', 'Kıyafet/Eski Ürün'),
    ('Kargolama', 'Kitap/Kargolama'), 
    ('SipIptal', 'Kitap/Sipariş İptal'), 
    ('KitapDegisim', 'Kitap/Değişim'), 
    ('KitapIade', 'Kitap/İade'), 
    ('KitapIptal', 'Kitap/İptal'), 
    ('KitapKargo', 'Kitap/Kargo'), 
    ('KitapTeslimat', 'Kitap/Teslimat'), 
    ('KitapHataliUrun', 'Kitap/Hatalı Ürün'), 
    ('KitapEksikUrun', 'Kitap/Eksik Ürün')
]
)
    status = models.CharField(max_length=20, choices=TICKET_STATUS_CHOICES, default='OPEN')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.ticket_id:
            self.ticket_id = self.generate_unique_order_id()
        super(SupportTicket, self).save(*args, **kwargs)

    @staticmethod
    def generate_unique_order_id():
        date_str = datetime.datetime.now().strftime("%d%m%y")
        random_number = random.randint(1, 9999)
        ticket_id = f"DT-{date_str}-{random_number:04d}"

        while SupportTicket.objects.filter(ticket_id=ticket_id).exists():
            random_number = random.randint(1, 9999)
            ticket_id = f"DT-{date_str}-{random_number:04d}"

        return ticket_id

    def __str__(self):
        return f'{self.ticket_id}'
    
    class Meta:
        verbose_name = "Destek Talebi"
        verbose_name_plural = "Destek Talepleri"
        ordering = ['-created_at']



def upload_location(instance, filename):
    return f"support_uploads/{instance.ticket.member}/{filename}"

class SupportMessage(models.Model):
    ticket = models.ForeignKey(SupportTicket, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(Member, on_delete=models.CASCADE)  # assuming the sender is a User model instance
    message = models.TextField()
    file = models.FileField(upload_to=upload_location, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Destek Talebi Mesajları"
        verbose_name_plural = "Destek Talebi Mesajları"
        ordering = ['created_at']
