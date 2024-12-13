from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class NicknameValidator:

    def __call__(self, value):
        if not value.isalnum():
            raise ValidationError("Your nickname is invalid! Nicknames can only contain letters and digits.")

