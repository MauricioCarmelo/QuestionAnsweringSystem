import abc

class Task(metaclass=abc.ABCMeta):

    def __init__(self, id):
        self._id = id

    def get_id(self):
        return self._id

    @staticmethod
    @abc.abstractmethod
    def get_fields_for_technique():
        pass

