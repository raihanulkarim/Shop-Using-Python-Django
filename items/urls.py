from django.urls import path
from .views import HomeListView, ItemDetails,SearchView
urlpatterns = [
    path('', HomeListView.as_view(),name = 'home'),
    path('car/<int:pk>/', ItemDetails.as_view(), name = 'car-details'),
    path('search',SearchView.as_view(), name = 'search'),
]