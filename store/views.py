from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from webProject.context_processors import get_school
from django.http import JsonResponse
from django.views import generic
from products.models import *
from cart.models import *
from cart import views as cart_views
from schools.models import *
from members.models import *
from products.views import *
from members.urls import *
from store.models import *
from discounts.tasks import *
import json


@login_required
def index(request):
    update_discount_status(request)

    return render(request, 'store/index.html')


@login_required
def category(request):
    return render(request, 'store/category-list.html')

@login_required
def category_m(request, ProductCategoryID):
    campus_id = request.user.campus_id
    cat = ProductCategory.objects.get(ProductCategoryID=ProductCategoryID)
    subcat_ids = ProductSubCategory.objects.filter(ProductCategory=cat).values_list('ProductSubCategoryID', flat=True)
    active_products_by_cat = Products.objects.filter(
        product_state='Aktif', 
        school=get_school(),
        ProductSubCategoryID__in=subcat_ids
        ).prefetch_related('productprices_set')
    
    for product in active_products_by_cat:
        campus_price = product.productprices_set.filter(campusPrice=campus_id).first()
        if campus_price:
            product.display_price = campus_price
        else:
            product.display_price = product.productprices_set.first()

    context = {
        'active_products_by_cat': active_products_by_cat,
        'cat': cat,
    }

    return render(request, 'store/category.html', context)

@login_required
def category_p(request, ProductSubCategoryID):
    campus_id = request.user.campus_id
    subcat = ProductSubCategory.objects.get(ProductSubCategoryID=ProductSubCategoryID)
    active_products_by_cat = Products.objects.filter(
        product_state='Aktif', 
        school=get_school(),
        ProductSubCategoryID=subcat
        ).prefetch_related('productprices_set')
    
    for product in active_products_by_cat:
        campus_price = product.productprices_set.filter(campusPrice=campus_id).first()
        if campus_price:
            product.display_price = campus_price
        else:
            product.display_price = product.productprices_set.first()

    context = {
        'active_products_by_cat': active_products_by_cat,
        'subcat': subcat,
    }

    return render(request, 'store/category.html', context)
    

@login_required
def product(request, ProductID):
    product = Products.objects.get(school=get_school(), ProductID=ProductID, product_type='Tekil')

    related_products = Products.objects.filter(ProductSubCategoryID=product.ProductSubCategoryID).exclude(ProductID=ProductID)[:4]

    campus_based_price = product.productprices_set.filter(campusPrice=request.user.campus_id)
    if campus_based_price.exists():
        cb_price = campus_based_price.first()
    else:
        cb_price = product.productprices_set.first()

    pcontext = {
        'product': product,
        'related_products': related_products,
        'cb_price': cb_price,
    }

    return render(request, 'store/product.html', pcontext)

@login_required
def combproduct(request, ProductID):
    product = Products.objects.get(school=get_school(), ProductID=ProductID, product_type='Kombin')
    combproduct = CombinationProduct.objects.filter(Product=product)

    campus_based_price = product.productprices_set.filter(campusPrice=request.user.campus_id)
    if campus_based_price.exists():
        cb_price = campus_based_price.first()
    else:
        cb_price = product.productprices_set.first()

    pcontext = {
        'product': product,
        'combproduct': combproduct,
        'cb_price': cb_price,
    }

    return render(request, 'store/combproduct.html', pcontext)





@login_required
def cart(request):
    update_discount_status(request)
    cart_views.apply_special_discount(request)
    cart_views.apply_coupon(request)
    return render(request, 'store/cart.html')


@login_required
@require_POST
def add_to_cart(request):
    product_id = request.POST.get('id')
    product_title = request.POST.get('title')
    product_size = request.POST.get('size')
    quantity = int(request.POST.get('qty'))
    price = request.POST.get('price')

    # Fetch the product and size-based stock
    product = get_object_or_404(Products, ProductID=product_id)
    size_stock = get_object_or_404(SizeBasedStocks, products=product, size__ProductSize=product_size)

    # Retrieve or create a cart for the user
    cart, created = Cart.objects.get_or_create(member=request.user)

    # Create or update CartItem
    cart_item, created = CartItems.objects.get_or_create(
        cart=cart, 
        product=product, 
        size_stock=size_stock,
        defaults={'quantity': quantity}
    )
    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    
    cart_item.save()
    cart_views.apply_special_discount(request)
    cart_views.apply_coupon(request)

    # Prepare the response
    response_data = {
        'status': 'success',
        'message': 'Product added to cart successfully',
        'cart_total_items': cart.user_cart.count()  # Count total items in user's cart
    }
    return JsonResponse(response_data), redirect('product', product_id)


@login_required
@require_POST
def add_combined_to_cart(request):
    # Extract data from the AJAX request
    product_id = request.POST.get('product_id')
    title = request.POST.get('title')
    qty = request.POST.get('qty')
    price = request.POST.get('price')
    combined_choices = request.POST.get('combined_choices')

    # Convert combined_choices JSON string to a Python list of dictionaries
    combined_choices = json.loads(combined_choices)

    # Create a new Cart instance (if needed) and save it
    # Assuming you have a Cart model to manage the cart
    cart, created = Cart.objects.get_or_create(member=request.user)

    # Create CartItems instance for the main product
    cart_item = CartItems(cart=cart, is_combined_product=True, product_id=product_id, quantity=qty)
    cart_item.save()

    # Loop through the combined choices and create CombinedProductChoice instances
    for choice in combined_choices:
        combination_product_category_id = choice['combcat']
        selected_product_id = choice['product_id']
        selected_product_size_id = choice['size_id']

        # Create a CombinedProductChoice instance
        combined_choice = CombinedProductChoice(
            cart_item=cart_item,
            combination_product_category_id=combination_product_category_id,
            selected_product_id=selected_product_id,
            size_stock_id=selected_product_size_id,
        )
        combined_choice.save()

    # You can update the cart's other properties here (e.g., discounts, shipping, etc.)

    # Prepare the response data
    response_data = {'status': 'success', 'message': 'Ürünler Başarıyla Sepete Eklendi', 'cart_total_items': cart.user_cart.count()}

    return JsonResponse(response_data)


@login_required
@require_POST
def delete_from_cart(request):
    cart_item_id = request.POST.get('cart_item_id')
    print("Received request to delete cart item:", cart_item_id)
    try:
        cart_item = CartItems.objects.get(id=cart_item_id, cart__member=request.user)
        cart_item.delete()
        return JsonResponse({'deleted': True})
    except CartItems.DoesNotExist:
        return JsonResponse({'deleted': False}, status=404)
    except Exception as e:
        return JsonResponse({'deleted': False, 'error': str(e)}, status=500)








@login_required
def pages(request, page_url):
    school_pages = SchoolPages.objects.get(school=get_school(), page_url=page_url) 

    page_context = {
        'school_pages': school_pages,
    }

    return render(request, 'store/pages.html', page_context)


@login_required
def search(request):
    query = request.GET.get('search')
    products = Products.objects.filter(school=get_school(), product_web_name__icontains=query)

    context = {
        'search_products': products,
        'query': query,
    }

    return render(request, 'store/search.html', context)


def get_districts(request):
    city_id = request.GET.get('city_id')
    districts = District.objects.filter(city_id=city_id).values('id', 'name')
    return JsonResponse(list(districts), safe=False)