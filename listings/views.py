from django.shortcuts import render, get_object_or_404
from .models import listing
from django.core.paginator import Paginator
from .choices import price_choices, state_choices, bedroom_choices

def index(request):
    listings_list = listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings_list, 3)
    page = request.GET.get('page')

    context = {
        'listings' : paginator.get_page(page),
    }

    return render(request, 'listings/listings.html', context)

def listinglist(request, listing_id):
    listing1 = get_object_or_404(listing, pk=listing_id)

    context = {
        'listing' : listing1
    }

    return render(request, 'listings/listing.html', context)

def search(request):

    query_set_list = listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_set_list = query_set_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_set_list = query_set_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_set_list = query_set_list.filter(state__iexact=state)

    # Bedrroms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_set_list = query_set_list.filter(bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET: 
        price = request.GET['price']
        if price:
            query_set_list = query_set_list.filter(price__lte=price)

    context = {
        'state_choices' : state_choices,
        'bedroom_choices' : bedroom_choices,
        'price_choices' : price_choices,
        'listings' : query_set_list,
        'values' : request.GET
    }

    return render(request, 'listings/search.html', context)

  