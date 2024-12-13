from django import forms

from traveler.models import Traveler


class TravelerBaseForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = ('nickname', 'email', 'country',)
        widgets = {
            'nickname': forms.TextInput(attrs={'placeholder': 'Enter a unique nickname...'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter a valid email address..'}),
            'country': forms.TextInput(attrs={'placeholder': 'Enter a country code like <BGR>...'})
        }
        labels = {
            'nickname': 'Nickname:',
            'email': 'Email:',
            'country': 'Country:'
        }


class TravelerCreateForm(TravelerBaseForm):
    pass
