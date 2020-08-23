from django.urls import path
from .views import HomeListView, ItemDetails
urlpatterns = [
    path('', HomeListView.as_view(),name = 'home'),
    path('car/<int:pk>/', ItemDetails.as_view(), name = 'car-details'),
]