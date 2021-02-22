from django.shortcuts import render,redirect
from django.core.paginator import Paginator

from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from .models import Listing,Contact
from .choices import *
# Create your views here.
def listings(request):
    listings=Listing.objects.all()
    paginator=Paginator(listings,2)
    page=request.GET.get('page')
    page_listings=paginator.get_page(page)
    context={
        'listings':page_listings
    }
    return render(request,'listings/listings.html',context)

def listing(request,listings_id):
    if Listing.objects.filter(id=listings_id).exists():
        listing = Listing.objects.get(id=listings_id)
        context = {
            'listing': listing
        }

        return render(request, 'listings/listing.html', context)
    else:

        return render(request, 'page_not_found.html')

def search(request):
    listings = Listing.objects.all()

    #keywords
    if "keywords" in request.GET:
        keywords= request.GET['keywords']
        if keywords:
            listings=listings.filter(description__icontains= keywords )

    # city
    if "city" in request.GET:
        city = request.GET['city']
        if city:
            listings = listings.filter(city__iexact=city)

    # state
    if "state" in request.GET:
        state = request.GET['state']
        if state:
            listings = listings.filter(state=city)

    # bedrooms
    if "bedrooms" in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            listings = listings.filter(bedrooms__lte=bedrooms)#lte=less than eqalto,gte=greater than equalto
    #price
    if "price" in request.GET:
        price = request.GET['price']
        if price:
            listings = listings.filter(price__lte=price)  # lte=less than eqalto,gte=greater than equalto

    context = {
        'listings': listings,
        'state_choices':state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'values':request.GET,
    }


    return render(request, 'listings/search.html',context)

def contact(request):
    if request.method== 'POST':

        listing=request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']

        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        if user_id=='None':
            user_id=0
        contact_obj=Contact(listing=listing,listing_id=listing_id,name=name,email=email,phone=phone,message=message,user_id=user_id)
        contact_obj.save()
        return redirect ('listings')
    else:
        pass

class ListingCreate(CreateView):
    model=Listing
    fields='__all__'
    success_url ='/listings'

class ListingUpdate(UpdateView):
    model=Listing
    fields='__all__'
    success_url ='/listings'

class ListingDelete(DeleteView):
    model=Listing
    fields='__all__'
    success_url = reverse_lazy('listings')