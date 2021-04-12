import abc

class DatasetReader:

    def __init__(self, name, path, fields_to_read):
        self.name = name
        self.path = path
        self.fields_to_read = fields_to_read

    @abc.abstractmethod
    def load_entries(self):
        pass
