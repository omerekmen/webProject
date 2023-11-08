from products.models import *
import random



def default(request, school=1):
    categories = ProductCategory.objects.all()
    subcategories = ProductSubCategory.objects.all() 

    active_products = Products.objects.filter(product_state='Aktif', school=school)
    active_comb_products = Products.objects.filter(product_state='Aktif', product_type='Kombin', school=school)

    random_products = list(active_products)
    random.shuffle(random_products)

    schools = Schools.objects.get(school_id=school)

    return {
        'categories': categories,
        'subcategories': subcategories,

        'active_products': active_products, 
        'active_comb_products': active_comb_products, 

        'random_products': random_products,

        'schools': schools,
    }