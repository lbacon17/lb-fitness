from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


def shop_all(request):
    """This view renders all items on the main shop page"""
    shop_items = Product.objects.all()
    categories = Category.objects.all()
    query = None
    category = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey == 'lower_name'
                shop_items = shop_items.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            shop_items = shop_items.order_by(sortkey)

        # checks whether category parameter exists and splits categories
        # into a list and filters each one if it does
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            shop_items = shop_items.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search terms!")
                return redirect(reverse('shop'))
            
            queries = Q(name__icontains=query)
            shop_items = shop_items.filter(queries)

    sort_by = f'{sort}_{direction}'

    context = {
        'shop_items': shop_items,
        'search_term': query,
        'categories': categories,
        'sort_by': sort_by,
    }

    return render(request, 'shop/shop.html', context)