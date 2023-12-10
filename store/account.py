from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from webProject.context_processors import get_school
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse, HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from products.models import *
from cart.models import *
from schools.models import *
from members.models import *
from products.views import *
from members.urls import *
from store.models import *
from orders.models import *

@login_required
def account(request):
    return render(request, 'store/account.html')

@require_POST
def address_update(request):
    user = request.user

    city_name = request.POST.get('city')
    city = get_object_or_404(City, id=city_name)
    district_name = request.POST.get('district')
    district = get_object_or_404(District, name=district_name)
    address = request.POST.get('delivery-address')
    phone = request.POST.get('phone')
    phone_numeric = ''.join(filter(str.isdigit, phone))

    invoice_city_name = request.POST.get('city')
    invoice_city = get_object_or_404(City, id=invoice_city_name)
    invoice_district_name = request.POST.get('district')
    invoice_district = get_object_or_404(District, name=invoice_district_name)
    invoice_address = request.POST.get('invoice-address')
    invoice_phone = request.POST.get('invoice-phone')
    invoice_phone_numeric = ''.join(filter(str.isdigit, invoice_phone))

    delivery_common_fields = {
        'recipient_name': request.POST.get('first-name'),
        'recipient_lastname': request.POST.get('last-name'),

        'Country': request.POST.get('country'),
        'City': city,
        'District': district,
        'FullAddress': address,
        'PostalCode': request.POST.get('zip'),

        'PhoneNumber': phone_numeric,
        'EMail': request.POST.get('email-address'),
    }
    
    invoice_common_fields = {
        'recipient_name': request.POST.get('first-name'),
        'recipient_lastname': request.POST.get('last-name'),

        'Country': request.POST.get('country'),
        'City': invoice_city,
        'District': invoice_district,
        'FullAddress': invoice_address,
        'PostalCode': request.POST.get('zip'),

        'PhoneNumber': invoice_phone_numeric,
        'EMail': request.POST.get('invoice-email-address'),

        'comp_name': request.POST.get('company-name'),
        'tax_office': request.POST.get('company-tax-office'),
        'tax_no': request.POST.get('company-tax-no'),
    }

    delivery_address, _ = MemberAddress.objects.get_or_create(
        member=user,
        AddressType='Delivery',
        defaults=delivery_common_fields
    )
    for field, value in delivery_common_fields.items():
        setattr(delivery_address, field, value)
    delivery_address.save()

    if request.POST.get('different-address') == 'on':
        invoice_address, _ = MemberAddress.objects.get_or_create(
            member=user,
            AddressType='Invoice',
            defaults=invoice_common_fields
        )
        for field, value in invoice_common_fields.items():
            setattr(invoice_address, field, value)
        invoice_address.save()

    return redirect('account')


@require_POST
def account_details_update(request):
    if request.method == 'POST':
        user = request.user

        

        campus_id = request.POST.get('user_school')
        level_id = request.POST.get('levelSelect')
        class_id = request.POST.get('classSelect')
        phone = request.POST.get('phone')

        campus = get_object_or_404(SchoolCampus, pk=campus_id) if campus_id else user.campus_id
        level = get_object_or_404(StudentLevels, pk=level_id) if level_id else user.level_id
        sclass = get_object_or_404(Class, pk=class_id) if class_id else user.class_id
        phone_numeric = ''.join(filter(str.isdigit, phone))

        common_fields = {
            'username': request.POST.get('username'),
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),

            'email': request.POST.get('email'),
            'phone_number': phone_numeric,

            'birth_date': request.POST.get('user_bdate'),
            'user_gender': request.POST.get('user_gender'),

            'campus_id': campus,
            'level_id': level,
            'class_id': sclass,
        }
        
        member, _ = Member.objects.get_or_create(
            member_id=user.member_id,
            defaults=common_fields
        )
        for field, value in common_fields.items():
            setattr(member, field, value)
        member.save()
        messages.success(request, "Kullanıcı bilgileriniz başarıyla güncellendi.")
    return HttpResponseRedirect('/account/#account')

@require_POST
def password_update(request):
    if request.method == 'POST':
        user = request.user

        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if current_password and new_password:
            if check_password(current_password, user.password):
                if new_password == confirm_password:
                    user.set_password(new_password)
                    user.save()
                    messages.success(request, "Mevcut şifrenizbaşarıyla değiştirildi.")
                    return redirect('login')
                else:
                    messages.error(request, "Girmiş olduğunuz şifreler uyuşmuyor, lütfen kontrol ederek tekrar deneyiniz.")
            else:
                messages.error(request, "Mevcut şifrenizi yanlış girdiniz.")
    return HttpResponseRedirect('/account/#account')


def get_order_details(request):
    order_id = request.GET.get('order_id')
    order = get_object_or_404(Orders, OrderID=order_id)
    return render(request, 'store/order-detail.html', {'order': order})


def get_student_class(request):
    level_id = request.GET.get('level_id')
    classes = Class.objects.filter(LevelName_id=level_id).values('id', 'ClassName')
    return JsonResponse(list(classes), safe=False)


def pass_change(PasswordChangeView):
    template_name = "registration/password_change_form.html"
    return