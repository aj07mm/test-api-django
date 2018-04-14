from rest_framework import serializers
from project.apps.three_your_mind.models import Printer



class PrinterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Printer
        fields = "__all__"
