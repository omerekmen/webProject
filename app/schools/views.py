from django.shortcuts import render
from django.http import JsonResponse
from .models import SchoolPages


# Create your views here.
def get_page_content(request):
    page_title = request.GET.get('page_title')
    if page_title:
        try:
            page = SchoolPages.objects.get(page_title=page_title)
            return JsonResponse({'content': page.page_content})
        except SchoolPages.DoesNotExist:
            return JsonResponse({'error': 'Page not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def fetch_content_for_modal(request):
    page_url = request.GET.get('page_url')
    try:
        page = SchoolPages.objects.get(page_url=page_url)
        content = page.page_content
        return JsonResponse({'content': content})
    except SchoolPages.DoesNotExist:
        return JsonResponse({'error': 'Content not found'}, status=404)
