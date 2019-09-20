from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import GuitarInfo, BRAND_CHOICES

def index(request):
    obj_list = GuitarInfo.objects.all()
    bc = BRAND_CHOICES

    query = request.GET.get('q')
    price_from = request.GET.get('price_from')
    price_to = request.GET.get('price_to')
    price = request.GET.get('price_order')

    filtered_results = GuitarInfo.objects.filter(Q(brand_choice=query) & Q(price__range=(price_from, price_to)))
    if price:
        filtered_results = filtered_results.order_by(price)
    
    paginator = Paginator(filtered_results, 20)
    page = request.GET.get('page')
    items = paginator.get_page(page)


    return render(request, 'entries/index.html', {'obj_list': obj_list, 
                                                  'filter': filtered_results,
                                                  'bc': bc,
                                                  'items': items
                                                  })