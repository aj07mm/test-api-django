from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator


class User(AbstractUser):
    pass


class Book(models.Model):
    title = models.CharField(max_length=255, blank=False)
    isbn_number = models.CharField(max_length=13, unique=True, blank=False)

    def __str__(self):
        return u"%s" % self.title


class Rate(models.Model):
    stars = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    review = models.TextField(blank=False)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, null=False, blank=False,
    )

    def __str__(self):
        return u"%s - %s" % self.book, self.stars
