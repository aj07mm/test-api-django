from rest_framework import status
from rest_framework.test import APITestCase
from project.apps.three_your_mind import serializers

from . import factories


class APIViewsetTests(APITestCase):

    """
    Testing viewset default methods
        http://www.django-rest-framework.org/api-guide/viewsets/

            list(self, request)
            create(self, request)
            retrieve(self, request, pk=None)
            update(self, request, pk=None)
            partial_update(self, request, pk=None)
            destroy(self, request, pk=None)


    class PrinterSerializer(NestingSerializer, serializers.ModelSerializer):

        class Meta:
            model = Printer
            fields = [
                "name",
                "min_production_time",
                "max_production_time"
            ]
            # The ‘nesting’ option should be used by the
            nesting = {
                "productionTime": {
                    "minimum" : "min_production_time",
                    "maximum" : "max_production_time",
                },
            }

    """
    @classmethod
    def setUpTestData(cls):
        cls.printer = factories.PrinterFactory.create(
            name="asdasd",
            min_production_time=123,
            max_production_time=123,
        )

    def test_create_printer(self):
        response = self.client.post(
            '/api/printers/',
            {
                'name': 'Lexmark',
                'min_production_time': 85,
                'max_production_time': 85,
            },
            format='json',
        )
        assert response.data['name'] == 'Lexmark'
        assert response.data['productionTime']['minimum'] == 85
        assert response.data['productionTime']['maximum'] == 85
        assert response.status_code == status.HTTP_201_CREATED



    # ---- test serializers --- #


    def test_create_printer_with_1_level_nested_dict(self):
        serializer = serializers.Printer1stLevelSerializer(instance=self.printer)
        assert serializer.data['name'] == 'asdasd'
        assert serializer.data['productionTime']['minimum'] == 123
        assert serializer.data['productionTime']['maximum'] == 123

    def test_create_printer_with_2_level_nested_dict(self):
        serializer = serializers.Printer2ndLevelSerializer(instance=self.printer)
        assert serializer.data['name'] == 'asdasd'
        assert serializer.data['productionTime']['minimum'] == 123
        assert serializer.data['productionTime']['maximum'] == 123
        assert serializer.data['productionTime']['medium'] == 123

    def test_create_printer_with_3_level_nested_dict(self):
        serializer = serializers.Printer3ndLevelSerializer(instance=self.printer)
        assert serializer.data['name'] == 'asdasd'
        assert serializer.data['productionTime']['minimum'] == 123
        assert serializer.data['productionTime']['maximum'] == 123
        assert serializer.data['productionTime']['medium']['mirror_xyz'] == 123
