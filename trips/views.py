from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from DjangoBasicsRetakeExam.utils import get_user_obj
from trips.forms import TripCreateForm
from trips.models import Trip


# Create your views here.


class TripCreateView(CreateView):
    model = Trip
    form_class = TripCreateForm
    template_name = 'create-trip.html'
    success_url = reverse_lazy('all-trips')

    def form_valid(self, form):
        form.instance.traveler = get_user_obj()
        return super().form_valid(form)


class TripDetailView(DetailView):
    model = Trip
    template_name = 'details-trip.html'
    pk_url_kwarg = 'trip_pk'
