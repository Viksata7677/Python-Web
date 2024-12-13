from django.urls import path

from traveler.views import TravelerCreateView, TravelerDetailView

urlpatterns = [
    path('create/', TravelerCreateView.as_view(), name='create-traveler'),
    path('details/', TravelerDetailView.as_view(), name='details-traveler'),
]