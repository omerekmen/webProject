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

def check_specialdiscount_usage(discount, member):
    usage_count, created = SpecialDiscountUsage.objects.get_or_create(discount=discount, member=member)
    return usage_count

def apply_special_discount(request):
    member = request.user
    member_campus = member.campus_id
    cart = get_object_or_404(Cart, member=member)

    if cart.SpecialDiscountStatus != 'Özel İndirim Yok':
        pass
    else:
        try:
            discounts = SpecialDiscount.objects.filter(discountStatus = True).filter(
                Q(member__isnull=True, campus__isnull=True) |
                Q(member=member) |
                Q(campus=member.campus_id)
            )

            member_discounts = discounts.filter(member=member).order_by('-discountCreatedDate')
            campus_discounts = discounts.filter(campus=member_campus).order_by('-discountCreatedDate')
            all_discounts = discounts.filter(member__isnull=True, campus__isnull=True).order_by('-discountCreatedDate')

            for md in member_discounts:
                print(md)

            if discounts:
                if member_discounts:
                    for md in member_discounts:
                        sd_usage = check_specialdiscount_usage(md, member)
                        if sd_usage.count_usage < md.discountPerPerson:
                            print(f'Valla da az {sd_usage.count_usage} / {md.discountPerPerson}')
                            cart.SpecialDiscountApplied = md
                            sd_usage.count_usage += 1
                            sd_usage.save()
                            print(f'Şimdi Güncelleme {sd_usage.count_usage} / {md.discountPerPerson}')
                            break
                elif campus_discounts:
                    for cd in campus_discounts:
                        cd_usage = check_specialdiscount_usage(cd, member)
                        if cd_usage.count_usage < cd.discountPerPerson:
                            cart.SpecialDiscountApplied = cd
                            cd_usage.count_usage += 1
                            cd_usage.save()
                            break
                elif all_discounts:
                    for all in campus_discounts:
                        all_usage = check_specialdiscount_usage(all, member)
                        if all_usage.count_usage < all.discountPerPerson:
                            cart.SpecialDiscountApplied = all
                            all_usage.count_usage += 1
                            all_usage.save()
                            break

                cart.SpecialDiscountStatus = 'Özel İndirim Uygulandı'

            else:
                cart.SpecialDiscountStatus = 'Özel İndirim Yok'
                cart.SpecialDiscountApplied = None

            cart.save()
            
        except SpecialDiscount.DoesNotExist:
            pass


def apply_coupon(request):
    if request.method == 'POST':
        coupon_code = request.POST.get('coupon_code')
        cart_id = request.POST.get('cart_id')
        member = request.user

        cart = get_object_or_404(Cart, cart_id=cart_id)

        if cart.CouponCode == coupon_code:
            messages.success(request, "Kupon Kodu zaten uygulanmış.")
            return redirect('cart')

        try:
            potential_coupons = DiscountCoupon.objects.filter(
                discountCouponCode=coupon_code,
                discountStatus=True,
            )

            coupon = potential_coupons.filter(
                Q(member__isnull=True, campus__isnull=True) |  # No specific user or campus
                Q(member=member) |                            # Specific member
                Q(campus=member.campus_id)                    # Specific campus
            ).get()

            usage_count, created = DiscountCouponUsage.objects.get_or_create(discount=coupon, member=member)

        except DiscountCoupon.DoesNotExist:
            messages.error(request, "Kupon Kodu Geçersiz!")
            return redirect('cart')  # Adjust as per your URL name

        if coupon.discountRemainingNumber == 0:
            messages.error(request, "İndirim Kuponunun kullanım limitine ulaşıldı!")
            return redirect('cart')
        
        if usage_count.count_usage == coupon.discountPerPerson:
            messages.error(request, "İndirim Kuponunun maximum sayıda faydalandınız!")
            return redirect('cart')

        cart.CouponCode = coupon.discountCouponCode
        cart.apply_discount_coupon()
        usage_count.count_usage += 1
        usage_count.save()
        cart.save()

        messages.success(request, "Kupon Kodu başarıyla uygulandı.")
        return redirect('cart')

    else:
        return redirect('cart')

