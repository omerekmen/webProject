from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse
from django.db import transaction

from products.models import *
from members.models import *
from schools.models import *
from store.models import *
from cart.models import *
from .models import *

from products.views import *
from django.urls import reverse
from members.urls import *
from discounts.tasks import *

from payment.iyzico import iyzico
import json

@login_required
def checkout(request):
    update_discount_status(request)
    return render(request, 'store/checkout.html')

def get_city_name(city_id):
    city = get_object_or_404(City, id=city_id)
    return city.name or None

def get_district_name(district_id):
    district = get_object_or_404(District, id=district_id)
    return district.name

def get_city(city_id):
    city = get_object_or_404(City, id=city_id)
    return city

def get_district(district_id):
    district = get_object_or_404(District, id=district_id)
    return district

@require_POST
def create_order(request):
    print('SİPARİŞİ OLUŞTUR BUTONUNA BASILDI')
    if request.method == 'POST':
        user = request.user
        cart = Cart.objects.filter(member=user).first()

        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        country = request.POST.get('country')
        city = request.POST.get('citySelect')
        city_name = get_city_name(city)
        district = request.POST.get('districtSelect')
        district_name = get_district_name(district)
        address = request.POST.get('delivery-address')
        zip = request.POST.get('zip')
        phone = request.POST.get('phone')
        email = request.POST.get('email-address')

        different_address = request.POST.get('different-address')
        save_address = request.POST.get('saveas-default-address')
        order_notes = request.POST.get('order-notes')

        invoice_city = invoice_city_name = invoice_district = invoice_district_name = ""
        invoice_address = invoice_phone = invoice_email = comp_name = tax_office = tax_number = ""

        if different_address:
            invoice_city = request.POST.get('invoicecitySelect')
            invoice_city_name = get_city_name(invoice_city)
            invoice_district = request.POST.get('invoicedistrictSelect')
            invoice_district_name = get_district_name(invoice_district)
            invoice_address = request.POST.get('invoice-address')
            invoice_phone = request.POST.get('invoice-phone')
            invoice_email = request.POST.get('invoice-email-address')
            comp_name = request.POST.get('invoice-company-name')
            tax_office = request.POST.get('invoice-company-tax-office')
            tax_number = request.POST.get('invoice-company-tax-no')


        last_login_date = user.last_login.strftime('%Y-%m-%d %H:%M:%S') if user.last_login else None
        registration_date = user.registration_date.strftime('%Y-%m-%d %H:%M:%S') if user.registration_date else None


        conversation_id = str(iyzico.create_conversation_id())
        price = str(cart.prod_total_price())
        paid_price = str(cart.total_price())
        basket_id = cart.cart_id
        callback_url = request.build_absolute_uri(reverse('return_from_iyzico'))
        buyer=iyzico.create_buyer(
                buyerid=str(user.member_id),
                name=user.first_name,
                surname=user.last_name,
                gsm_number='+90' + str(user.phone_number),
                email=user.email,
                identity_number=str(user.username) if len(user.username)>6 else '11111111111',
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

            if item.is_combined_product:
                pass
            elif item.is_set_product:
                pass
            else:
                size_based_stock = SizeBasedStocks.objects.filter(products=item.product, size=item.size_stock.size).first()
                if not size_based_stock or size_based_stock.sale_stock < item.quantity:
                    print(f"Not enough stock for {item.product.product_name}. Only {size_based_stock.sale_stock if size_based_stock else 0} left.")
                    return JsonResponse({
                        'error': f'{item.product.product_name} için sadece {size_based_stock.sale_stock if size_based_stock else 0} adet stok mevcut. Lütfen sepetinizi kontrol ediniz.'
                    })
            
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

        common_fields = {
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
            'different_address': different_address == 'on',
            'save_address': save_address == 'on',
            'conversation_id': conversation_id,
            'token': token,
        }

        temp_order_details, _ = TempOrderDetails.objects.get_or_create(
            member=user, 
            defaults=common_fields
            )

        for field, value in common_fields.items():
            setattr(temp_order_details, field, value)
        temp_order_details.save()

        if json_content['status'] == 'success':
            form_content = json_content.get('checkoutFormContent')
            payment_page_url = json_content['paymentPageUrl']
            return JsonResponse({'formContent': form_content, 'paymentPageUrl': payment_page_url})
        else:
            # Handle failure
            error_message = json_content.get('errorMessage')
            return JsonResponse({'error': error_message})
    return render(request, 'store/order.html')

@csrf_exempt
def return_from_iyzico(request):
    return redirect('get_payment_details')

@csrf_exempt
def get_payment_details(request):
    if request.user.is_authenticated:
        member_id = request.user.member_id
    else:
        member_id = None
    get_member = Member.objects.filter(member_id=member_id).first()
    order_detail = TempOrderDetails.objects.filter(member=get_member).last()

    if order_detail is None:
        messages.error(request, 'Sipariş Bilgileriniz Alınırken Bir Hata Oluştu. Lütfen Tekrar Deneyiniz.')
        return redirect('order_error')
    
    city_instance, created = City.objects.get_or_create(name=order_detail.city_name)
    district_instance, created = District.objects.get_or_create(name=order_detail.district_name, city=city_instance)
    invoice_city_instance, created = City.objects.get_or_create(name=order_detail.invoice_city_name)
    invoice_district_instance, created = District.objects.get_or_create(name=order_detail.invoice_district_name, city=invoice_city_instance)
    formatted_phone_number = ''.join(filter(str.isdigit, order_detail.phone))
    formatted_invoice_phone_number = ''.join(filter(str.isdigit, order_detail.invoice_phone))
    conversation_id = order_detail.conversation_id
    token = order_detail.token

    payment = iyzico.retrieve_checkout_form(conversation_id, token)
    payment = payment.read().decode('utf-8')
    json_content = json.loads(payment)

    print('**************************')
    print(json_content)
    print('**************************')

    if json_content['status'] == 'success':
        try:
            with transaction.atomic():
                user = request.user
                cart = Cart.objects.get(member=user.member_id)  # Retrieve user's cart
                
                if order_detail.save_address == True:
                    city_name = order_detail.city_name
                    city = get_object_or_404(City, name=city_name)
                    district_name = order_detail.district_name
                    district = get_object_or_404(District, name=district_name)

                    delivery_common_fields = {
                        'recipient_name': order_detail.first_name,
                        'recipient_lastname': order_detail.last_name,

                        'Country': order_detail.country,
                        'City': city,
                        'District': district,

                        'FullAddress': order_detail.address,
                        'PostalCode': order_detail.zip,

                        'PhoneNumber': ''.join(filter(str.isdigit, order_detail.phone)),
                        'EMail': order_detail.email,
                    }
                    delivery_address, _ = MemberAddress.objects.get_or_create(
                        member=user,
                        AddressType='Delivery',
                        defaults=delivery_common_fields
                    )
                    for field, value in delivery_common_fields.items():
                        setattr(delivery_address, field, value)
                    delivery_address.save()

                    if order_detail.different_address == True:
                        invoice_city_name = order_detail.invoice_city_name
                        invoice_city = get_object_or_404(City, name=invoice_city_name)
                        invoice_district_name = order_detail.invoice_district_name
                        invoice_district = get_object_or_404(District, name=invoice_district_name)

                        invoice_common_fields = {
                            'recipient_name': order_detail.first_name,
                            'recipient_lastname': order_detail.last_name,

                            'Country': order_detail.country,
                            'City': invoice_city,
                            'District': invoice_district,
                            'FullAddress': order_detail.invoice_address,
                            'PostalCode': order_detail.zip,

                            'PhoneNumber': ''.join(filter(str.isdigit, order_detail.invoice_phone)),
                            'EMail': order_detail.invoice_email,

                            'comp_name': order_detail.comp_name,
                            'tax_office': order_detail.tax_office,
                            'tax_no': order_detail.tax_number,
                        }
                        invoice_address, _ = MemberAddress.objects.get_or_create(
                            member=user,
                            AddressType='Invoice',
                            defaults=invoice_common_fields
                        )
                        for field, value in invoice_common_fields.items():
                            setattr(invoice_address, field, value)
                        invoice_address.save()


                # Create an order instance
                order = Orders.objects.create(
                    Member=user,

                    OrderCargoFee = cart.shipping_cost(),
                    SpecialDiscountStatus = cart.SpecialDiscountStatus,
                    SpecialDiscount = cart.SpecialDiscount,
                    CouponCode = cart.CouponCode,
                    CouponDiscount = cart.CouponDiscount,

                    OrderNote = order_detail.order_notes,

                    # Add other necessary fields
                )
                OrderPayment.objects.create(
                    Order=order,
                    PaymentProvider='iyzico',
                    PaymentId=json_content.get('paymentId', ''),
                    ConversationId=json_content.get('conversationId', ''),
                    FraudStatus=str(json_content.get('fraudStatus', '')),
                    Installment=json_content.get('installment', 1),
                    Currency=json_content.get('currency', 'TRY'),
                    Price=json_content.get('price', 0),
                    PaidPrice=json_content.get('paidPrice', 0),
                    iyziCommissionRateAmount=json_content.get('iyziCommissionRateAmount', 0),
                    iyziCommissionFee=json_content.get('iyziCommissionFee', 0),
                    MerchantPayoutAmount=json_content.get('merchantPayoutAmount', 0),
                    CardType=json_content.get('cardType', ''),
                    CardAssociation=json_content.get('cardAssociation', ''),
                    CardFamily=json_content.get('cardFamily', '')
                )

                # Create an order address instance
                OrderAddress.objects.create(
                    Order=order,
                    AddressType = 'Teslimat',

                    recipient_name = order_detail.first_name,
                    recipient_lastname = order_detail.last_name,
                    Country = order_detail.country,
                    City = city_instance,
                    District = district_instance,
                    FullAddress = order_detail.address,
                    PostalCode = order_detail.zip,
                    PhoneNumber = formatted_phone_number,
                    EMail = order_detail.email,
                )

                if order_detail.different_address == True:
                    OrderAddress.objects.create(
                        Order=order,
                        AddressType = 'Fatura',

                        recipient_name = order_detail.first_name,
                        recipient_lastname = order_detail.last_name,
                        Country = order_detail.country,
                        City = invoice_city_instance,
                        District = invoice_district_instance,
                        FullAddress = order_detail.invoice_address,
                        PostalCode = order_detail.zip,
                        PhoneNumber = formatted_invoice_phone_number,
                        EMail = order_detail.invoice_email,
                        comp_name = order_detail.comp_name,
                        tax_office = order_detail.tax_office,
                        tax_no = order_detail.tax_number,
                    )
                else:
                    OrderAddress.objects.create(
                        Order=order,
                        AddressType = 'Fatura',

                        recipient_name = order_detail.first_name,
                        recipient_lastname = order_detail.last_name,
                        Country = order_detail.country,
                        City = city_instance,
                        District = district_instance,
                        FullAddress = order_detail.address,
                        PostalCode = order_detail.zip,
                        PhoneNumber = formatted_phone_number,
                        EMail = order_detail.email,
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
                            order_prod = order_item,
                            combination_product_category = combined_choice.combination_product_category,
                            selected_product = combined_choice.selected_product,
                            size_stock = combined_choice.size_stock,
                        )

                    
                    ################################################################
                    ###################### STOCK UPDATE LOGIC ######################
                    ################################################################

                    if item.is_combined_product:
                        for combined_choice in item.combinedproductchoice_set.all():
                            print('A:',combined_choice)
                            size_descriptor = combined_choice.size_stock
                            print('Sipariş Öncesi:', size_descriptor)
                            size_item = size_descriptor.size

                            size_based_stock = SizeBasedStocks.objects.filter(products=combined_choice.selected_product, size=size_item).first()
                            if size_based_stock:
                                size_based_stock.real_stock = max(0, size_based_stock.real_stock - item.quantity)
                                size_based_stock.sale_stock = max(0, size_based_stock.sale_stock - item.quantity)
                                size_based_stock.save()
                            
                            print('Sipariş Sonrası:', size_descriptor)

                    elif item.is_set_product:
                        # If the product is a combined or set product, handle stock update logic accordingly
                        # This part depends on how you manage stock for combined and set products
                        pass
                    else:
                        size_descriptor = item.size_stock
                        print(size_descriptor)
                        size_item = size_descriptor.size
                        print(size_item)

                        size_based_stock = SizeBasedStocks.objects.filter(products=item.product, size=size_item).first()
                        if size_based_stock:
                            size_based_stock.real_stock = max(0, size_based_stock.real_stock - item.quantity)
                            size_based_stock.sale_stock = max(0, size_based_stock.sale_stock - item.quantity)
                            size_based_stock.save()

                    ################################################################
                    ###################### STOCK UPDATE LOGIC ######################
                    ################################################################


                cart.delete()
                order_detail.delete()
                Cart.objects.get_or_create(member=request.user)

            messages.success(request, 'Ödeme Başarılı ve Sipariş Oluşturuldu.')
            order_id = order.OrderID
            return redirect('order', OrderID=order_id)
        except Exception as e:
            messages.error(request, f'Sipariş oluşturulurken hata: {e}')
            return JsonResponse({'error': str(e)})
            
    else:
        error_message = json_content.get('errorMessage')
        return JsonResponse({'error': error_message})

@login_required
def order(request, OrderID):
    order = get_object_or_404(Orders, OrderID=OrderID)
    order_delivery_address = OrderAddress.objects.filter(Order=order, AddressType='Teslimat').first()
    order_invoice_address = OrderAddress.objects.filter(Order=order, AddressType='Fatura').first()

    context = {
        'order': order,
        'order_delivery_address': order_delivery_address,
        'order_invoice_address': order_invoice_address,
    }
    return render(request, 'store/order.html', context)

@login_required
def order_details(request, OrderID):
    order = get_object_or_404(Orders, OrderID=OrderID)
    order_delivery_address = OrderAddress.objects.filter(Order=order, AddressType='Teslimat').first()
    order_invoice_address = OrderAddress.objects.filter(Order=order, AddressType='Fatura').first()

    context = {
        'order': order,
        'order_delivery_address': order_delivery_address,
        'order_invoice_address': order_invoice_address,
    }
    return render(request, 'store/order-details.html', context)

@login_required
def order_error(request):
    return render(request, 'store/order-error.html')
