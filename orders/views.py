from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from products.models import *
from cart.models import *
from schools.models import *
from members.models import *
from store.models import *
from .models import *
from products.views import *
from members.urls import *
from payment.iyzico import iyzico
from django.db import transaction
import json

@login_required
def checkout(request):
    return render(request, 'store/checkout.html')

def get_city(city_id):
    city = get_object_or_404(City, id=city_id)
    return city.name

def get_district(district_id):
    district = get_object_or_404(District, id=district_id)
    return district.name

@require_POST
def create_order(request):
    if request.method == 'POST':
        user = request.user
        cart = Cart.objects.filter(member=user).first()

        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        country = request.POST.get('country')
        city = request.POST.get('citySelect')
        city_name = get_city(city)
        district = request.POST.get('districtSelect')
        district_name = get_district(district)
        address = request.POST.get('delivery-address')
        zip = request.POST.get('zip')
        phone = request.POST.get('phone')
        email = request.POST.get('email-address')

        invoice_city = request.POST.get('invoicecitySelect')
        invoice_city_name = get_city(invoice_city)
        invoice_district = request.POST.get('invoicedistrictSelect')
        invoice_district_name = get_district(invoice_district)
        invoice_address = request.POST.get('invoice-address')
        invoice_phone = request.POST.get('invoice-phone')
        invoice_email = request.POST.get('invoice-email-address')
        comp_name = request.POST.get('invoice-company-name')
        tax_office = request.POST.get('invoice-company-tax-office')
        tax_number = request.POST.get('invoice-company-tax-no')

        order_notes = request.POST.get('order-notes')

        different_address = request.POST.get('different-address')
        save_address = request.POST.get('ssaveas-default-address')


        last_login_date = user.last_login.strftime('%Y-%m-%d %H:%M:%S') if user.last_login else None
        registration_date = user.registration_date.strftime('%Y-%m-%d %H:%M:%S') if user.registration_date else None


        conversation_id = str(iyzico.create_conversation_id())
        price = str(cart.prod_total_price())
        paid_price = str(cart.total_price())
        basket_id = cart.cart_id
        callback_url = request.build_absolute_uri(reverse('get_payment_details'))
        buyer=iyzico.create_buyer(
                buyerid=str(user.member_id),
                name=user.first_name,
                surname=user.last_name,
                gsm_number='+90' + str(user.phone_number),
                email=user.email,
                identity_number=str(user.username),
                last_login_date=last_login_date,
                registration_date=registration_date,
                registration_address=address,
                city=city_name,
                country=country,
                zip_code=str(zip),
                ip=str(user.ip_address),
            )
        shipping_address=iyzico.create_address(
                contact_name=first_name + ' ' + last_name,
                city=city_name,
                country=country,
                address=address,
                zip_code=str(zip),
            )
        
        if request.POST.get('different-address') == 'on':
            billing_address=iyzico.create_address(
                    contact_name=comp_name,
                    city=invoice_city_name,
                    country=country,
                    address=invoice_address,
                    zip_code=str(zip),
                )
        else:
            billing_address=shipping_address

        basket_items = []
        for item in cart.user_cart.all():
            basket_items += iyzico.create_basket_item(
                    prod_id=str(item.product.ProductID),
                    name=item.product.product_web_name,
                    category1=item.product.ProductSubCategoryID.ProductCategory.CategoryName,
                    category2=item.product.ProductSubCategoryID.SubCategoryName,
                    price=str(item.total_price()),
                )
        
        payment_form = iyzico.initialize_checkout_form(
            conversation_id = conversation_id,
            price = price,
            paid_price = paid_price,
            basket_id=basket_id,
            callback_url=callback_url,
            buyer=buyer,
            shipping_address=shipping_address,
            billing_address=billing_address,
            basket_items=basket_items,
        )

        page = payment_form
        header = {'Content-Type': 'application/json'}
        payment = payment_form.read().decode('utf-8')
        json_content = json.loads(payment)
        print(json_content)
        token = json_content["token"]


        request.session['order_details'] = {
            'first_name': first_name,
            'last_name': last_name,
            'country': country,
            'city': city,
            'city_name': city_name,
            'district': district,
            'district_name': district_name,
            'address': address,
            'zip': zip,
            'phone': phone,
            'email': email,

            'invoice_city': invoice_city,
            'invoice_city_name': invoice_city_name,
            'invoice_district': invoice_district,
            'invoice_district_name': invoice_district_name,
            'invoice_address': invoice_address,
            'invoice_phone': invoice_phone,
            'invoice_email': invoice_email,
            'comp_name': comp_name,
            'tax_office': tax_office,
            'tax_number': tax_number,

            'order_notes': order_notes,
            'different_address': different_address,
            'save_address': save_address,

            'conversation_id': conversation_id,
            'token': token,
        }

        if json_content['status'] == 'success':
            form_content = json_content.get('checkoutFormContent')
            return JsonResponse({'formContent': form_content})
        else:
            # Handle failure
            error_message = json_content.get('errorMessage')
            return JsonResponse({'error': error_message})
    return render(request, 'store/order.html')

def get_payment_details(request):
    order_details = request.session.get('order_details')
    if order_details is None:
        messages.error(request, 'Sipariş Bilgileriniz Alınırken Bir Hata Oluştu. Lütfen Tekrar Deneyiniz.')
        return redirect('order')
    else:
        conversation_id = order_details['conversation_id']
        token = order_details['token']

        payment = iyzico.retrieve_checkout_form(conversation_id, token)
        payment = payment.read().decode('utf-8')
        json_content = json.loads(payment)

        print(json_content)
        if json_content['status'] == 'success':
            try:
                with transaction.atomic():
                    user = request.user
                    cart = Cart.objects.get(member=user)  # Retrieve user's cart

                    # Create an order instance
                    order = Order.objects.create(
                        Member=user,

                        OrderCargoFee = cart.shipping_cost(),
                        SpecialDiscountStatus = cart.SpecialDiscountStatus,
                        SpecialDiscount = cart.SpecialDiscount,
                        CouponCode = cart.CouponCode,
                        CouponDiscount = cart.CouponDiscount,

                        OrderNote = order_details['order_notes'],

                        # Add other necessary fields
                    )

                    # Create an order address instance
                    OrderAddress.objects.create(
                        order=order,
                        AddressType = 'Teslimat',

                        recipient_name = order_details['first_name'],
                        recipient_lastname = order_details['last_name'],
                        Country = order_details['country'],
                        City = order_details['city'],
                        District = order_details['district'],
                        FullAddress = order_details['address'],
                        PostalCode = order_details['zip'],
                        PhoneNumber = order_details['phone'],
                        EMail = order_details['email'],
                    )

                    if order_details['different_address'] == 'on':
                        OrderAddress.objects.create(
                            order=order,
                            AddressType = 'Fatura',

                            recipient_name = order_details['first_name'],
                            recipient_lastname = order_details['last_name'],
                            Country = order_details['country'],
                            City = order_details['invoice_city'],
                            District = order_details['invoice_district'],
                            FullAddress = order_details['invoice_address'],
                            PostalCode = order_details['zip'],
                            PhoneNumber = order_details['invoice_phone'],
                            EMail = order_details['invoice_email'],
                            comp_name = order_details['comp_name'],
                            tax_office = order_details['tax_office'],
                            tax_number = order_details['tax_number'],
                        )
                    else:
                        OrderAddress.objects.create(
                            order=order,
                            AddressType = 'Fatura',

                            recipient_name = order_details['first_name'],
                            recipient_lastname = order_details['last_name'],
                            Country = order_details['country'],
                            City = order_details['city'],
                            District = order_details['district'],
                            FullAddress = order_details['address'],
                            PostalCode = order_details['zip'],
                            PhoneNumber = order_details['phone'],
                            EMail = order_details['email'],
                        )

                    # For each item in the cart, create an order item
                    for item in cart.user_cart.all():
                        order_item = OrderProducts.objects.create(
                            Order = order,
                            Product = item.product,
                            is_combined_product = item.is_combined_product,
                            is_set_product = item.is_set_product,
                            selected_size = item.size_stock,
                            Quantity = item.quantity,
                            prod_old_price = item.old_price(),
                            prod_sale_price = item.single_price(),
                            discounted_sale_price = item.total_price(),
                        )

                        for combined_choice in item.combinedproductchoice_set.all():
                            OrderCombinedProductChoice.objects.create(
                                order_item = order_item,
                                combination_product_category = combined_choice.combination_product_category,
                                selected_product = combined_choice.selected_product,
                                size_stock = combined_choice.size_stock,
                            )

                    # Clear the cart after creating the order
                    cart.user_cart.all().delete()

                messages.success(request, 'Ödeme Başarılı ve Sipariş Oluşturuldu.')
                return JsonResponse({'payment': json_content})
            except Exception as e:
                messages.error(request, f'Sipariş oluşturulurken hata: {e}')
                return JsonResponse({'error': str(e)})
                
        else:
            error_message = json_content.get('errorMessage')
            return JsonResponse({'error': error_message})

@login_required
def order(request):
    return render(request, 'store/order.html')
