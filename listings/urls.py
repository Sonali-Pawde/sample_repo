from django.urls import path
from . import views
urlpatterns=[
    path('',views.listings,name='listings'),
    path('<int:listings_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path('contact', views.contact, name='contact'),
    path('add',views.ListingCreate.as_view(),name='listing-add'),
    path('<int:pk>/update',views.ListingUpdate.as_view(),name='listing-update'),
    path('<int:pk>/delete',views.ListingDelete.as_view(),name='listing-delete'),

]