from rest_framework import serializers
from django.core.urlresolvers import reverse
from project.apps.restaurants.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name')
    profile_url = serializers.SerializerMethodField()

    def get_profile_url(self, obj):
        return reverse('profile_detail', kwargs={'profile_id': obj.uuid})

    class Meta(object):
        model = Profile
        fields = "__all__"
