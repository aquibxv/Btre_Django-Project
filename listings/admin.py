from django.contrib import admin
from .models import listing


# we add things/properties related to how things are displayed
class ListingAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_published', 'price', 'list_date', 'realtor']
    list_display_links = ['id', 'title']
    list_filter = ['realtor', 'price']
    search_fields = ['title', 'address', 'city', 'state', 'zipcode', 'price ']
    list_per_page = 20

# Registering the model here
admin.site.register(listing, ListingAdmin)