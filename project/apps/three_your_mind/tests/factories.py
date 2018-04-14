import factory
from project.apps.three_your_mind.models import Printer


class PrinterFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Printer
