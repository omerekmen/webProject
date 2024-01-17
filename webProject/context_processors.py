from products.models import *
from schools.models import *
from members.models import *
from cart.models import *
from store.models import *
from orders.models import *
import random


def get_school():
    school = 1
    return school

def get_school_id(request):
    subdomain = request.get_host().split('.')[0]
    subdomain_to_school = {
        'bahcesehir': 1,
        'mektebim': 2,
    }
    school_id = subdomain_to_school.get(subdomain, 1)
    return school_id

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def default(request, school=get_school()):
    host = request.get_host().split('.')
    subdomain = request.get_host().split('.')[0]
    subdomain_to_school = {
        'bahcesehir': 1,
        'mektebim': 2,
    }
    school_id = subdomain_to_school.get(subdomain, 1)

    schools = Schools.objects.get(school_id=school_id)
    school_main_page_popup = SchoolPopup.objects.filter(school=school_id, popup_page="index").first()
    school_reg_page_popup = SchoolPopup.objects.filter(school=school_id, popup_page="intro").first()
    school_prod_page_popup = SchoolPopup.objects.filter(school=school_id, popup_page="product").first()


    path = request.path
    parts = path.strip('/').split('/')
    sublink = parts[0]
    scl = subdomain_to_school.get(sublink, 1)


    cities = City.objects.all()
    levels = StudentLevels.objects.all()


    user = request.user.is_authenticated
    user_ip = get_client_ip(request)
    if user:
        campus_id = request.user.campus_id
    else:
        campus_id = None
    
    if user:
        delivery_address = MemberAddress.objects.filter(member=request.user, AddressType='Delivery').first()
        invoice_address = MemberAddress.objects.filter(member=request.user, AddressType='Invoice').first()
    else:
        delivery_address = None
        invoice_address = None

    categories = ProductCategory.objects.filter()
    subcategories = ProductSubCategory.objects.filter()

    active_products = Products.objects.filter(
        product_state='Aktif', 
        school=schools
        ).prefetch_related('productprices_set')
    
    active_comb_products = Products.objects.filter(product_state='Aktif', product_type='Kombin', school=schools)


    for product in active_products:
        campus_price = product.productprices_set.filter(campusPrice=campus_id).first()
        if campus_price:
            product.display_price = campus_price
        else:
            product.display_price = product.productprices_set.first()

    if user:
        cart = Cart.objects.get(member=request.user)
        cartitems = CartItems.objects.filter(cart=cart)
    else:
        cart = None
        cartitems = None

    if user:
        user_orders = Orders.objects.filter(Member=request.user)
    else:
        user_orders = None

    random_products = list(active_products)
    random.shuffle(random_products)


    return {
        'user': user,
        'user_ip': user_ip,
        'user_orders': user_orders,
        'delivery_address': delivery_address, 
        'invoice_address': invoice_address,

        # 'site': site,
        'subdomain': subdomain,

        'categories': categories,
        'subcategories': subcategories,

        'active_products': active_products, 
        'active_comb_products': active_comb_products, 

        'random_products': random_products,

        'cart': cart,
        'cartitems': cartitems,

        'schools': schools,
        'school_main_page_popup': school_main_page_popup,
        'school_reg_page_popup': school_reg_page_popup,
        'school_prod_page_popup': school_prod_page_popup,
        'cities': cities,
        'levels': levels,
        'sc': scl,
    }