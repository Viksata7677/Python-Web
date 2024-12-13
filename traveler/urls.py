from django.urls import path

from traveler.views import TravelerCreateView, TravelerDetailView, TravelerEditView, TravelerDeleteView

urlpatterns = [
    path('create/', TravelerCreateView.as_view(), name='create-traveler'),
    path('details/', TravelerDetailView.as_view(), name='details-traveler'),
    path('edit/', TravelerEditView.as_view(), name='edit-traveler'),
    path('delete/', TravelerDeleteView.as_view(), name='delete-traveler'),
]