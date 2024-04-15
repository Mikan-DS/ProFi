import typing
from enum import Enum, auto

from ProOrientation.models import (
    Employee,
)


class FilterFieldType(Enum):
    STR = auto()
    INT = auto()
    FOREIGN = auto()

    @classmethod
    def from_value(cls, value):
        return cls(value).name




auto_fields_map: typing.Dict[FilterFieldType, typing.Tuple[str, str]] = {
    FilterFieldType.INT: ("AutoField", "IntegerField"),
    FilterFieldType.STR: ("CharField", "EmailField"),
    FilterFieldType.FOREIGN: ("OneToOneField", "ForeignKey"),
}

def get_auto_field_type(type_name):
    for field_type, db_field_types in auto_fields_map.items():
        if type_name in db_field_types:
            return field_type
    return None



class FilterField:
    def __init__(self, field_verbose, field_name, field_type):
        self.field_verbose = field_verbose
        self.field_name = field_name
        self.field_type: FilterFieldType = field_type

    @property
    def json(self):
        return {
            "field_verbose": self.field_verbose,
            "field_name": self.field_name,
            "field_type_id": self.field_type.value,
            "field_type": self.field_type.name,
        }

class Filter:
    filters_map = []
    def __init__(self, model):
        self.model = model

        self.fields = []

        for field in model._meta.fields:
            field_type = get_auto_field_type(field.__class__.__name__)
            if field_type:
                self.fields.append(FilterField(field.verbose_name, field.name, field_type))

        Filter.filters_map.append(self)

    @property
    def name(self):
        return self.model.__name__

    @property
    def json(self):
        return {
            "name": self.name,
            "verbose": self.model._meta.verbose_name,
            "verbose_plural": self.model._meta.verbose_name_plural,
            "fields": self.fields_json
        }

    @property
    def fields_json(self):
        return list(map(lambda x: x.json, self.fields))

    @classmethod
    def get_filter(cls, name):
        for filter in Filter.filters_map:
            if filter.name == name:
                return filter
        return None


Filter(Employee)
