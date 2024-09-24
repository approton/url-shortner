from django.db import models

# Create your models here.
from django.db import models
import string, random

# Model for storing long and short URLs
class URL(models.Model):
    long_url = models.URLField(max_length=500)
    short_url = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.short_url} -> {self.long_url}"

    # Generate a random string for the short URL
    @staticmethod
    def generate_short_url():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

