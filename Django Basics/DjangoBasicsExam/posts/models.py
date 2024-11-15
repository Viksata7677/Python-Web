from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from author.models import Author  # Ensure you import the Author model


def validate_title_length(value):
    if not (5 <= len(value) <= 50):
        raise ValidationError("Title should be between 5 and 50 characters.")


class Post(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
        error_messages={
            'unique': "Oops! That title is already taken. How about something fresh and fun?"
        },
        validators=[validate_title_length],
    )
    image_url = models.URLField(
        help_text="Share your funniest furry photo URL!"
    )
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    def __str__(self):
        return self.title
