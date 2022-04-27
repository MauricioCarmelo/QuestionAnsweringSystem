import abc


class Technique(metaclass=abc.ABCMeta):
    def __init__(self, name):
        self._name = name
        self.input_field_mapping = None

    def get_name(self):
        return self._name

    def set_input_field_mapping(self, input_field_mapping):
        self.input_field_mapping = input_field_mapping

    def _has_input_field_mapped(self, field_name):
        return field_name in self.input_field_mapping

    def get_actual_field_name(self, field_name):
        if self._has_input_field_mapped(field_name):
            return self.input_field_mapping[field_name]
        return field_name

    @abc.abstractmethod
    def run(self, resource_entries):
        pass

    def setup(self):
        pass

    def train(self, train_set, dev_set, test_set, resource_articles):
        pass

    def validate(self, dev_set):
        pass
