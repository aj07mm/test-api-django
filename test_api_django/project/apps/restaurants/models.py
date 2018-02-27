from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=256)
    opens_at = models.DateTimeField(null=True)
    closes_at = models.DateTimeField(null=True)
