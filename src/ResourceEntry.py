class ResourceEntry:
    def __init__(self, fields=None):
        if not fields:
            self.field_value_mapping = {}
        else:
            self.field_value_mapping = {x: None for x in fields}

    def get_field_value_mapping(self):
        return self.field_value_mapping

    def get_value(self, field):
        if field in self.field_value_mapping:
            return self.field_value_mapping[field]
        else:
            return None

    def add_mapped_value(self, field, value):
        self.field_value_mapping[field] = value

    def append_dictionary_values(self, d):
        for key, value in d.items():
            self.add_mapped_value(key, value)
