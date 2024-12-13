from django.urls import path

from common.views import IndexPage, AllTripsPage

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('all-trips/', AllTripsPage.as_view(), name='all-trips'),
]