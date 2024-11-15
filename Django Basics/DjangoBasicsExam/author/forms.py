from django import forms
from django.core.exceptions import ValidationError
from .models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'passcode', 'pets_number', 'info', 'image_url']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter your first name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter your last name...'}),
            'passcode': forms.PasswordInput(attrs={'placeholder': 'Enter 6 digits...'}),
            'pets_number': forms.NumberInput(attrs={'placeholder': 'Enter the number of your pets...'}),
            'info': forms.Textarea(attrs={'placeholder': 'Add additional information about yourself...'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Enter your profile image URL...'}),
        }
        help_texts = {
            'passcode': "Your passcode must be a combination of 6 digits",
        }

