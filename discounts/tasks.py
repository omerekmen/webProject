from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import *
from cart.models import *

def update_discount_status(request):
    member = request.user
    specialdiscounts = SpecialDiscount.objects.all()
    discountcoupons = DiscountCoupon.objects.all()
    cart = get_object_or_404(Cart, member=member)
    today = timezone.now()
    
    for discount in specialdiscounts:
        if discount.discountStartDate and discount.discountEndDate:
            discount.discountStatus = discount.discountStartDate <= today <= discount.discountEndDate
        elif discount.discountStartDate and not discount.discountEndDate:
            discount.discountStatus = discount.discountStartDate <= today
        elif not discount.discountStartDate and discount.discountEndDate:
            discount.discountStatus = today <= discount.discountEndDate
        discount.save()  
        
    for discount in discountcoupons:
        if discount.discountStartDate and discount.discountEndDate:
            discount.discountStatus = discount.discountStartDate <= today <= discount.discountEndDate
        elif discount.discountStartDate and not discount.discountEndDate:
            discount.discountStatus = discount.discountStartDate <= today
        elif not discount.discountStartDate and discount.discountEndDate:
            discount.discountStatus = today <= discount.discountEndDate
        discount.save()  

    cart.apply_discount_coupon()

    
