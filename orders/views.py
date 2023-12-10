from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from webProject.context_processors import get_school
from django.http import JsonResponse
from products.models import *
from cart.models import *
from schools.models import *
from members.models import *
from store.models import *
from products.views import *
from members.urls import *
from payment.iyzico import iyzico
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
        comp_name = request.POST.get('invoice-company-name')
        tax_office = request.POST.get('invoice-company-tax-office')
        tax_number = request.POST.get('invoice-company-tax-no')

        order_notes = request.POST.get('order-notes')


        last_login_date = user.last_login.strftime('%Y-%m-%d %H:%M:%S') if user.last_login else None
        registration_date = user.registration_date.strftime('%Y-%m-%d %H:%M:%S') if user.registration_date else None


        conversation_id = str(iyzico.create_conversation_id())
        price = str(cart.prod_total_price())
        paid_price = str(cart.total_price())
        basket_id = cart.cart_id
        callback_url = request.build_absolute_uri(reverse('order'))
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
        
        print(conversation_id)
        print('***********************')
        print(price)
        print('***********************')
        print(paid_price)
        print('***********************')
        print(basket_id)
        print('***********************')
        print(callback_url)
        print('***********************')
        print(buyer)
        print('***********************')
        print(shipping_address)
        print('***********************')
        print(billing_address)
        print('***********************')
        print(basket_items)


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

        return HttpResponse(json_content["checkoutFormContent"])
    return render(request, 'store/order.html')

@login_required
def order(request):
    return render(request, 'store/order.html')
