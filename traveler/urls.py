from django.urls import path

from traveler.views import TravelerCreateView

urlpatterns = [
    path('create/', TravelerCreateView.as_view(), name='create-traveler'),
]