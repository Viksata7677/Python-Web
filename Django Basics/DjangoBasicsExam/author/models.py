from django.db import models
from django.core.exceptions import ValidationError


def validate_letters_only(value):
    if not value.isalpha():
        raise ValidationError("Your name must contain letters only!")


def validate_passcode(value):
    if len(value) != 6 or not value.isdigit():
        raise ValidationError("Your passcode must be exactly 6 digits!")


class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[validate_letters_only],
        help_text="First name should contain only letters.",
    )
    last_name = models.CharField(
        max_length=50,
        validators=[validate_letters_only],
        help_text="Last name should contain only letters.",
    )
    passcode = models.CharField(
        max_length=6,
        validators=[validate_passcode],
        help_text="Your passcode must be a combination of 6 digits"
    )
    pets_number = models.PositiveSmallIntegerField()
    info = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
