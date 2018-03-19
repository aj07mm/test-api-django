from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from project.apps.twyla.utils import get_current_user
from project.validators import ISBNValidator


class User(AbstractUser):
    pass


class FollowUserModel(models.Model):
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        editable=False,
        related_name='%(class)s_created'
    )

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and user.is_authenticated:
            self.created_by = user
        super(FollowUserModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Book(FollowUserModel):
    title = models.CharField(max_length=255, blank=False)
    isbn_number = models.CharField(
        max_length=13,
        unique=True,
        blank=False,
        validators=[ISBNValidator]
    )

    def __str__(self):
        return u"%s" % self.title


class Rate(FollowUserModel):
    stars = models.PositiveIntegerField(validators=[MaxValueValidator(5)])
    review = models.TextField(blank=False)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, null=False, blank=False,
    )

    def __str__(self):
        return u"%s - %s" % (self.book, self.stars)
