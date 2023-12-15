from django.utils import timezone
from .models import *

def update_discount_status():
    specialdiscounts = SpecialDiscount.objects.all()
    discountcoupons = DiscountCoupon.objects.all()
    today = timezone.now()
    for discount in specialdiscounts:
        if discount.discountStartDate and discount.discountEndDate:
            discount.discountStatus = discount.discountStartDate <= today <= discount.discountEndDate
        elif discount.discountStartDate and not discount.discountEndDate:
            discount.discountStatus = discount.discountStartDate <= today
        elif not discount.discountStartDate and discount.discountEndDate:
            discount.discountStatus = today <= discount.discountEndDate
        specialdiscounts.save()

    for discount in discountcoupons:
        if discount.discountStartDate and discount.discountEndDate:
            discount.discountStatus = discount.discountStartDate <= today <= discount.discountEndDate
        elif discount.discountStartDate and not discount.discountEndDate:
            discount.discountStatus = discount.discountStartDate <= today
        elif not discount.discountStartDate and discount.discountEndDate:
            discount.discountStatus = today <= discount.discountEndDate
        discountcoupons.save()