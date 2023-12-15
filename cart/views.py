from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from discounts.models import *
from .models import *
import json

@csrf_exempt
def update_cart_quantity(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cart_item_id = data.get('cartItemId')
        new_quantity = data.get('quantity')

        try:
            cart_item = CartItems.objects.get(id=cart_item_id, cart__member=request.user)
            cart_item.quantity = new_quantity
            cart_item.save()

            return JsonResponse({'status': 'success', 'message': 'Quantity updated'})
        except CartItems.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Cart item not found'}, status=404)

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


def apply_coupon(request):
    if request.method == 'POST':
        coupon_code = request.POST.get('coupon_code')
        cart_id = request.POST.get('cart_id')

        cart = get_object_or_404(Cart, cart_id=cart_id)
        member = request.user

        print("Member:", member)
        print("Member's Campus ID:", member.campus_id)

        try:
            current_time = timezone.now()

            potential_coupons = DiscountCoupon.objects.filter(
                discountCouponCode=coupon_code,
                discountStatus=True,
                discountStartDate__lte=current_time,
                discountEndDate__gte=current_time,
            )

            coupon = potential_coupons.filter(
                Q(member__isnull=True, campus__isnull=True) |  # No specific user or campus
                Q(member=member) |                            # Specific member
                Q(campus=member.campus_id)                    # Specific campus
            ).get()

            print(coupon)

        except DiscountCoupon.DoesNotExist:
            messages.error(request, "Kupon Kodu Geçersiz!")
            return redirect('cart')  # Adjust as per your URL name

        # Apply the coupon
        cart.CouponCode = coupon.discountCouponCode
        # cart.apply_discount_coupon()
        cart.save()

        messages.success(request, "Kupon Kodu başarıyla uygulandı.")
        return redirect('cart')

    else:
        return redirect('cart')

