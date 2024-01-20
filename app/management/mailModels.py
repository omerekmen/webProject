from django.db import models

class MailSettings(models.Model):
    mail_id = models.AutoField(primary_key=True, verbose_name='Mail ID')
    mail_host = models.CharField(max_length=255, verbose_name='Mail Host')
    mail_port = models.IntegerField(verbose_name='Mail Port')
    mail_use_tls = models.BooleanField(default=True, verbose_name='Mail TLS')
    mail_username = models.CharField(max_length=255, verbose_name='Mail Username')
    mail_password = models.CharField(max_length=255, verbose_name='Mail Password')
    mail_from = models.CharField(max_length=255, verbose_name='Mail From')
    mail_def_from = models.CharField(max_length=255, verbose_name='Mail Default From')

    class Meta:
        verbose_name = 'Mail Ayarları'
        verbose_name_plural = 'Mail Ayarları'

    def __str__(self):
        return f'{self.mail_username}'