from products.models import *
from schools.models import *
from members.models import *
from cart.models import *
import random


def get_school():
    school = 1
    return school


def default(request, school=get_school()):
    path = request.path # For sublinks
    subdomain = request.get_host().split('.')[0] ### FOR SUBDOMAINs
    site = request.get_host()
    # Define a mapping of subdomains to school IDs
    subdomain_to_school = {
        'bahcesehir': 1,
        'mektebim': 2,
        # Add more subdomains and their corresponding school IDs as needed
    }

    # Get the school ID based on the subdomain, default to 1 if not found
    sc = subdomain_to_school.get(subdomain, 1)

    parts = path.strip('/').split('/')
    sublink = parts[0]
    scl = subdomain_to_school.get(sublink, 1)


    user = request.user.is_authenticated

    categories = ProductCategory.objects.filter()
    subcategories = ProductSubCategory.objects.filter()

    active_products = Products.objects.filter(product_state='Aktif', school=school)
    active_comb_products = Products.objects.filter(product_state='Aktif', product_type='Kombin', school=school)

    cart = Cart.objects.get(member=request.user)
    cartitems = CartItems.objects.filter(cart=cart)

    random_products = list(active_products)
    random.shuffle(random_products)

    schools = Schools.objects.get(school_id=school)

    return {
        'site': site,
        'subdomain': subdomain,

        'categories': categories,
        'subcategories': subcategories,

        'active_products': active_products, 
        'active_comb_products': active_comb_products, 

        'random_products': random_products,

        'cart': cart,
        'cartitems': cartitems,

        'user': user,

        'schools': schools,
        'sc': scl,
    }