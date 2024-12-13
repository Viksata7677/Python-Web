from django.core.validators import MinLengthValidator
from django.db import models

from traveler.validators import NicknameValidator


# Create your models here.


class Traveler(models.Model):
    nickname = models.CharField(max_length=30, validators=[MinLengthValidator(3), NicknameValidator()],
                                unique=True, help_text="*Nicknames can contain only letters and digits.")
    email = models.EmailField(max_length=30, unique=True)
    country = models.CharField(max_length=3, validators=[MinLengthValidator(3)],)
    about_me = models.TextField(null=True, blank=True)
