import abc


class Evaluator(metaclass=abc.ABCMeta):
    def __init__(self, dataset_name, task_id, task_name):
        self.dataset_name = dataset_name
        self.task_id = task_id
        self.task_name = task_name

    @abc.abstractmethod
    def evaluate_resource_entries(self, resource_entries):
        pass
