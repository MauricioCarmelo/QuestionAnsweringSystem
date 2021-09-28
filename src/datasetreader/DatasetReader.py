import abc
from src.ResourceEntry import ResourceEntry


class DatasetReader:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def new_resource_entry(self):
        resource_entry = ResourceEntry()
        return resource_entry

    @abc.abstractmethod
    def load_entries(self):
        """
        Load the information from the dataset.
        :return: dictionary with the values that were read from the dataset.
        """
        pass
