from django.urls import path

from trips.views import TripCreateView, TripDetailView

urlpatterns = [
    path('create/', TripCreateView.as_view(), name='create-trip'),
    path('<int:trip_pk>/', TripDetailView.as_view(), name='trip-detail'),
]