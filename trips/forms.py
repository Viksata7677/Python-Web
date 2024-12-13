from django import forms

from trips.models import Trip


class TripBaseForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ('destination', 'summary', 'start_date', 'duration', 'image_url')
        widgets = {
            'destination': forms.TextInput(attrs={'placeholder': 'Enter a short destination note...'}),
            'summary': forms.TextInput(attrs={'placeholder': 'Share your exciting moments...'}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'An optional image URL...'}),
        }
        labels = {
            'destination': 'Destination:',
            'summary': 'Summary:',
            'start_date': 'Started on:',
            'duration': 'Duration:',
            'image_url': 'Image URL:',
        }


class TripCreateForm(TripBaseForm):
    pass
