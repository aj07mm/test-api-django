from django.db import models


class Pet(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True)

class RecordLabel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, null=True)
    record_label = models.ForeignKey(RecordLabel, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
