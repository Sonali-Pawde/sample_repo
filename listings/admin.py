from django.contrib import admin

# Register your models here.
from listings.models import Listing

class Listing_Admin(admin.ModelAdmin):
    list_display=('id','title','price','realtor','is_published','list_date','sqft')
    list_display_links=('id','title')
    list_filter=('realtor',)
    list_editable=('is_published','price')
    search_fields=('title','description','address','state','city','zipcode','price')
    list_per_page= 25

admin.site.register(Listing,Listing_Admin)

