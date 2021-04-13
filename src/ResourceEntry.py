class ResourceEntry:
    def __init__(self, fields=None):
        if not fields:
            self.field_values = {}
        else:
            self.field_values = {x: None for x in fields}

    def add_mapped_value(self, key, value):
        self.field_values[key] = value
