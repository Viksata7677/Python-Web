from django.core.validators import MinLengthValidator
from django.db import models
from traveler.models import Traveler


# Create your models here.


class Trip(models.Model):
    destination = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    summary = models.TextField()
    start_date = models.DateField()
    duration = models.PositiveSmallIntegerField(default=1, help_text="*Duration in days is expected.")
    image_url = models.URLField(null=True, blank=True)
    traveler = models.ForeignKey(to=Traveler, on_delete=models.CASCADE)
