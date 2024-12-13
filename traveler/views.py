
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from DjangoBasicsRetakeExam.utils import get_user_obj
from traveler.forms import TravelerCreateForm
from traveler.models import Traveler


# Create your views here.


class TravelerCreateView(CreateView):
    model = Traveler
    template_name = 'create-traveler.html'
    form_class = TravelerCreateForm
    success_url = reverse_lazy('all-trips')


class TravelerDetailView(DetailView):
    model = Traveler
    template_name = 'details-traveler.html'

    def get_object(self, queryset=None):
        return get_user_obj()