"""Attribute mappings."""

def map(attribute_data, idp):
    attribute_map = {idp.id_attribute: idp.mapped_id_attribute}
    attribute_map.update(idp.attribute_map)
    for key, values in attribute_data.items():
        attribute = attribute_map.get(key, key)
        if not isinstance(attribute, Attribute):
            attribute = Attribute(attribute)
        value = attribute.map(values)
        if value is not None:
            yield attribute.name, value

class Attribute:
    """Base class for mapping a list of attribute values."""
    def __init__(self, name):
        self.name = name

    def map(self, values):
        """Return only the first value in a list of values."""
        return values and values[0]


class List(Attribute):
    """An attribute key whose values should be returned as a list."""
    def map(self, values):
        return values[:]


class NestedNameid(Attribute):
    """An attribute that's an object of a NameId structure."""
    def map(self, values):
        if not values:
            return None
        return values[0].get('NameID', {}).get('value')
