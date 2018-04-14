from rest_framework import serializers
from django.db import models
from project.apps.three_your_mind.models import Printer
from collections import OrderedDict, Iterable
from rest_framework.relations import Hyperlink, PKOnlyObject  # NOQA # isort:skip


class NestingSerializer(serializers.Serializer):

    def get_to_representation(self, instance):
        """
        Object instance -> Dict of primitive datatypes.
        """
        ret = OrderedDict()
        fields = self._readable_fields

        for field in fields:
            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            # We skip `to_representation` for `None` values so that fields do
            # not have to explicitly deal with that case.
            #
            # For related fields with `use_pk_only_optimization` we need to
            # resolve the pk value.
            check_for_none = attribute.pk if isinstance(attribute, PKOnlyObject) else attribute
            if check_for_none is None:
                ret[field.field_name] = None
            else:
                ret[field.field_name] = field.to_representation(attribute)

        return ret

    def replace_values(self, obj, current_value_sign, next_value):
        new_obj = OrderedDict()
            
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_obj[key] = self.replace_values(value, current_value_sign, next_value)
            return new_obj

        if obj == current_value_sign:
            return next_value
        return obj

    def to_representation(self, instance):
        ret = self.get_to_representation(instance)
        ret = { **ret, **self.Meta.nesting }

        fields = self._readable_fields
        # replace fields
        for field in fields:
            ret = self.replace_values(ret, field.field_name, field.get_attribute(instance))
        # replace nesting
        for key, value in self.Meta.nesting.items():
            ret = self.replace_values(ret, key, value)

        return ret
    

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
                "medium" : "bar",
            },
            "bar": 123
        }
