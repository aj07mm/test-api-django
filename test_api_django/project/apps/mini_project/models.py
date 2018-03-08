import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Topic(models.Model):
    name = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return u"%s" % self.name


class Profile(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    current_position = models.CharField(max_length=64, blank=True)
    about_you = models.TextField(max_length=255, blank=True)
    topics = models.ManyToManyField(Topic, blank=True, related_name='topics')

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_topics_ordered(self, profile):
        my_topics = self.topics.all()
        other_user_topics = profile.topics.all()

        common_topics = my_topics.filter(id__in=other_user_topics.values_list('id', flat=True))
        non_common_topics = my_topics.exclude(id__in=other_user_topics.values_list('id', flat=True))
        return list(common_topics) + list(non_common_topics)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
