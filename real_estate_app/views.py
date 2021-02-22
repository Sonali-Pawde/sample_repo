from django.shortcuts import render

from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import *

def home(request):
    return HttpResponse("<h1 style='text-align:center'>hello world</h1>")

def index(request):
    listings=Listing.objects.all().order_by("-list_date")[:3]
    context ={
        'listings':listings,
        'state_choices':state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request,'real_estate_app/index.html',context)

def about(request):
    realtors = Realtor.objects.all()
    if Realtor.objects.filter(is_mvp=True).exists():
        seller=Realtor.objects.filter(is_mvp=True)[0]
    else:
        seller=""

    return render(request,'real_estate_app/about.html',{'realtors':realtors,'seller':seller})
# Create your views here.
