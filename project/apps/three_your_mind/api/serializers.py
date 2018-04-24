from rest_framework import serializers
from django.db import models
from project.apps.three_your_mind.models import Printer
from collections import OrderedDict, Iterable
from rest_framework.relations import Hyperlink, PKOnlyObject  # NOQA # isort:skip


class NestingSerializer(serializers.Serializer):

    def get_nested_values(self, obj, nested_values=None):
        if nested_values is None:
            nested_values = []
        if isinstance(obj, dict):
            for key, value in obj.items():
                nested_values += self.get_nested_values(value)
            return nested_values
        return [obj]

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
        ret = { **self.Meta.nesting }
        fields = self._readable_fields
        nested_values = self.get_nested_values(ret)

        # replace fields
        for field in fields:
            if field.field_name not in nested_values:
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
            else:
                ret = self.replace_values(ret, field.field_name, field.get_attribute(instance))
        # replace nesting
        for key, value in self.Meta.nesting.items():
            ret = self.replace_values(ret, key, value)

        return ret

    def to_internal_value(self, data):
        """
        Dict of native values <- Dict of primitive datatypes.
        """
        if not isinstance(data, Mapping):
            message = self.error_messages['invalid'].format(
                datatype=type(data).__name__
            )
            raise ValidationError({
                api_settings.NON_FIELD_ERRORS_KEY: [message]
            }, code='invalid')

        ret = OrderedDict()
        errors = OrderedDict()
        fields = self._writable_fields

        for field in fields:
            validate_method = getattr(self, 'validate_' + field.field_name, None)
            primitive_value = field.get_value(data)
            try:
                validated_value = field.run_validation(primitive_value)
                if validate_method is not None:
                    validated_value = validate_method(validated_value)
            except ValidationError as exc:
                errors[field.field_name] = exc.detail
            except DjangoValidationError as exc:
                errors[field.field_name] = get_error_detail(exc)
            except SkipField:
                pass
            else:
                set_value(ret, field.source_attrs, validated_value)

        if errors:
            raise ValidationError(errors)

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
