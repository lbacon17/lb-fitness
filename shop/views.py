from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm
from .contexts import favourites
from haystack.query import SearchQuerySet
import json


def shop_autocomplete(request):
    if request.is_ajax():
        query = request.GET.get('term', '')
        shop_items = Product.objects.filter(friendly_name__icontains=query)
        search_suggestions = []
        for item in shop_items:
            place_json = item.friendly_name
            search_suggestions.append(place_json)
        data = json.dumps(search_suggestions)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def shop_all(request):
    """This view renders all items on the main shop page"""
    shop_items = Product.objects.all()
    categories = Category.objects.all()
    query = None
    category = None
    sort = None
    direction = None
    
    if request.GET:
        # checks whether a sort parameter exists and orders by selected
        # criteria if so
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

        # checks whether search query exists and returns results containing
        # keywords
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search terms!")
                return redirect(reverse('shop'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            shop_items = shop_items.filter(queries)

    sort_by = f'{sort}_{direction}'

    context = {
        'shop_items': shop_items,
        'search_term': query,
        'categories': categories,
        'sort_by': sort_by,
    }

    return render(request, 'shop/shop.html', context)


def item_info(request, item_id):
    item = get_object_or_404(Product, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'shop/item_info.html', context)


@login_required
def add_item(request):
    """This view allows the administrator to add an item to the shop"""
    if request.user.is_superuser:
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                new_item = form.save()
                messages.success(request, 'Your product was added to the store successfully.')
                return redirect(reverse('item_info', args=[new_item.id]))
            else:
                messages.error(request, 'There was an issue adding the product. Please ensure the form is valid.')
        else:
            form = ProductForm()
    else:
        messages.error(request, 'Sorry, you do not have permission to access this page.')
        return redirect(reverse('home'))
    
    template = 'shop/add_item.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_item(request, item_id):
    """This view allows an administrator to edit an item in the shop"""
    if request.user.is_superuser:
        item = get_object_or_404(Product, pk=item_id)
        if request.method == "POST":
            form = ProductForm(request.POST, request.FILES, instance=item)
            if form.is_valid():
                form.save()
                messages.success(request, 'Item was successfully updated.')
                return redirect (reverse('item_info', args=[item.id]))
            else:
                messages.error(request, 'There was an issue updating the item. Please make sure the form is valid.')
        else:
            form = ProductForm(instance=item)
    else:
        messages.error(request, 'Sorry, you do not have permission to access this page.')
        return redirect(reverse('home'))

    template = 'shop/edit_item.html'
    context = {
        'form': form,
        'item': item,
    }

    return render(request, template, context)


@login_required
def delete_item(request, item_id):
    if request.user.is_superuser:
        item = get_object_or_404(Product, pk=item_id)
        item.delete()
        messages.success(request, 'The product was successfully deleted from the shop.')
        return redirect(reverse('shop'))
    else:
        messages.error(request, 'Sorry, you do not have permission to perform this action.')
        return redirect(reverse('home'))


def favourite_item(request, item_id):
    item = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    favourites = request.session.get('favourites', [])
    if not item_id in favourites:
        favourites.append(item_id)
        messages.success(request, f'Added {item.item_id} to favourites.')

    request.session['favourites'] = favourites

    return redirect(redirect_url)
