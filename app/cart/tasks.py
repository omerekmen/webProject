from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import Cart

@shared_task
def delete_old_carts():
    two_days_ago = timezone.now() - timedelta(days=2)
    old_carts = Cart.objects.filter(updated_at__lt=two_days_ago) # pylint: disable=no-member
    count = old_carts.count()
    old_carts.delete()
    return f'Deleted {count} old carts'
