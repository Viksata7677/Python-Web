
from django.urls import reverse_lazy
from django.views.generic import CreateView

from traveler.forms import TravelerCreateForm
from traveler.models import Traveler


# Create your views here.


class TravelerCreateView(CreateView):
    model = Traveler
    template_name = 'create-traveler.html'
    form_class = TravelerCreateForm
    success_url = reverse_lazy('all-trips')
