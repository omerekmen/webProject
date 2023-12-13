from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CartItems
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
