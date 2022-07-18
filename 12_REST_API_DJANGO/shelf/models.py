from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=150)
    country = models.CharField(max_length=100, null=True, blank=True)
