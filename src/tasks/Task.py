import abc


class Task(metaclass=abc.ABCMeta):

    def __init__(self, id):
        self._id = id

    def get_id(self):
        return self._id

    @staticmethod
    @abc.abstractmethod
    def get_fields_for_technique():
        """
        Get the fields that are mandatory to execute the task. The source of the input fields can be the dataset or
        the result of another task.
        Field name convention:
            Dataset fields: 'dataset_*'
            Task fields: '*'
        :return: List of input fields that are mandatory for the task execution.
        """
        pass

    @abc.abstractmethod
    def run_technique(self, resource_entry):
        pass

    def validate_resource_entry(self, resource_entry):
        """
        Validates if the ResourceEntry instance contains all fields that are supposed to be used by the task.
        :return: True if all fields are present; False otherwise.
        """
        for field in self.get_fields_for_technique():
            if field not in resource_entry.get_field_value_mapping():
                return False
        return True
