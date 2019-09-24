from django.db import models
from django.urls import reverse

# Create your models here.
class Wish(models.Model):
    description = models.TextField(
        max_length=250,
        )

    def __str__(self):
        return self.model
    def get_absolute_url(self):
        return reverse('home')
