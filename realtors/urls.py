from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='realtors'),
    path('<int:id>', views.realtor, name='realtor'),
    path('add', views.realtor_add, name='realtor-add'),
    path('<int:id>/update', views.realtor_update, name='realtor-update'),
    path('<int:id>/delete', views.realtor_delete, name='realtor-delete'),
]