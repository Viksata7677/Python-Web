from django.db import models


class LanguageChoices(models.TextChoices):
    PYTHON = 'python', 'Python'
    JAVASCRIPT = 'js', 'JavaScript'
    C = 'c', 'C'
    C_PLUS_PLUS = 'c++', 'C++'
    OTHER = 'other', 'Other'