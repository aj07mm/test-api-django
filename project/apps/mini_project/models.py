import uuid
from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=12, blank=False)

    def __str__(self):
        return u"%s" % self.name


class Profile(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    current_position = models.CharField(max_length=64, blank=False)
    about_you = models.TextField(max_length=255, blank=False)
    topics = models.ManyToManyField(
        Topic,
        blank=False,
        related_name='topics',
    )

    def __str__(self):
        return u"%s - %s" % (self.uuid, self.get_full_name())

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_topics_ordered(self, profile):
        my_topics = self.topics.all()
        other_user_topics = profile.topics.all()

        common_topics = my_topics.filter(
            id__in=other_user_topics.values_list('id', flat=True)
        )
        non_common_topics = other_user_topics.exclude(
            id__in=my_topics.values_list('id', flat=True)
        )
        return list(common_topics) + list(non_common_topics)
