import abc
from src.SettingsYAML import SettingsYAML


class Evaluator(metaclass=abc.ABCMeta):
    def __init__(self, dataset_name, task_id, task_name, resource):
        self.dataset_name = dataset_name
        self.task_id = task_id
        self.task_name = task_name
        self.field_mapping, self.metrics = SettingsYAML.get_instance().get_evaluation_field_mapping_and_metrics(task_id)
        self.resource = resource
        pass

    @abc.abstractmethod
    def evaluate(self, resource_entries):
        pass
