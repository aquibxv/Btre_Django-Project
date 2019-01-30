from django.urls import path
from . import views

# listings/
urlpatterns = [
   path('', views.index, name="listings"),
   path('<int:listing_id>', views.listinglist, name="listing"),
   path('search', views.search, name="search"),
]