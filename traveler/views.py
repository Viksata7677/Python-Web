from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from traveler.forms import TravelerBaseForm
from traveler.models import Traveler


# Create your views here.


class TravelerCreateView(CreateView):
    model = Traveler
    template_name = 'create-traveler.html'
    form_class = TravelerBaseForm
    success_url = reverse_lazy('all-trips')
