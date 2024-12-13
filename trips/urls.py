from django.urls import path, include

from trips.views import TripCreateView, TripDetailView, TripEditView, TripDeleteView

urlpatterns = [
    path('create/', TripCreateView.as_view(), name='create-trip'),
    path('<int:trip_pk>/', include([
        path('details/', TripDetailView.as_view(), name='details-trip'),
        path('edit/', TripEditView.as_view(), name='edit-trip'),
        path('delete/', TripDeleteView.as_view(), name='delete-trip'),

    ]))
]