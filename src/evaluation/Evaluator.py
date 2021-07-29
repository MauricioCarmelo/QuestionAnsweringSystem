import abc
from src.Settings import Settings


class Evaluator(metaclass=abc.ABCMeta):
    def __init__(self, dataset_name, task_id, task_name):
        self.dataset_name = dataset_name
        self.task_id = task_id
        self.task_name = task_name
        self.field_mapping = Settings.get_instance().get_evaluation_field_mapping(task_id)

    @abc.abstractmethod
    def evaluate(self, resource_entries):
        pass
