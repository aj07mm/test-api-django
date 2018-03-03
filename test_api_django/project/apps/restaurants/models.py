import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Restaurant(models.Model):
    name = models.CharField(max_length=256)
    opens_at = models.DateTimeField(null=True)
    closes_at = models.DateTimeField(null=True)


class Topic(models.Model):
    name = models.CharField(max_length=30, blank=True)


class Profile(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    position = models.CharField(max_length=40, blank=True)
    description = models.TextField(max_length=500, blank=True)
    topics = models.ManyToManyField(Topic, related_name='topics')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

