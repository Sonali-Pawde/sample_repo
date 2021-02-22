from django.contrib import admin

# Register your models here.
from realtors.models import Realtor


class Realtor_Admin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'is_mvp', 'hire_date')
    list_display_links = ('hire_date',)
    # list_filter = ('name',)
    list_editable = ('is_mvp', 'name')
    search_fields = ('name', 'email', 'phone', 'hire_date')
    list_per_page = 10


admin.site.register(Realtor, Realtor_Admin)

