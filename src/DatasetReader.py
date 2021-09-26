import abc


class DatasetReader:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    @abc.abstractmethod
    def load_entries(self):
        """
        Load the information from the dataset.
        :return: dictionary with the values that were read from the dataset.
        """
        pass
