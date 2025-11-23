from model_v6 import Validated

class Quantity(Validated):
    def validate(self, instance, value):
        if value <= 0:
            raise ValueError('value must be > 0')
        return value
    
class NonBlank(Validated):
    def validate(self, instance, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError('value cannot be empty or blank')
        return value
    
    

class EntityMeta(type):
    
    def __init__(cls, name, bases, attr_dict):
        super().__init__(name, bases, attr_dict)
        for key, attr in attr_dict.items():
            if isinstance(attr, Validated):
                type_name = type(attr).__name__
                attr.storage_name = '_{}#{}'.format(type_name, key)

class Entity(metaclass=EntityMeta):
    """Class"""
    
