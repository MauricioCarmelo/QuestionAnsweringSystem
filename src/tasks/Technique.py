import abc


class Technique(metaclass=abc.ABCMeta):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    @abc.abstractmethod
    def run(self, resource_entries):
        pass

    def setup(self):
        pass

    def train(self, train_set):
        pass

    def validate(self, dev_set):
        pass
