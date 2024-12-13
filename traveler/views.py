
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from DjangoBasicsRetakeExam.utils import get_user_obj
from traveler.forms import TravelerCreateForm, TravelerEditForm
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


class TravelerEditView(UpdateView):
    model = Traveler
    template_name = 'edit-traveler.html'
    form_class = TravelerEditForm
    success_url = reverse_lazy('details-traveler')

    def get_object(self, queryset=None):
        return get_user_obj()


class TravelerDeleteView(DeleteView):
    template_name = 'delete-traveler.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_user_obj()