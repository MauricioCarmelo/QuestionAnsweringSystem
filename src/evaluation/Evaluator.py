import abc
from src.Settings import Settings
from src.SettingsYAML import SettingsYAML
from sklearn.metrics import f1_score


class Evaluator(metaclass=abc.ABCMeta):
    def __init__(self, dataset_name, task_id, task_name):
        self.dataset_name = dataset_name
        self.task_id = task_id
        self.task_name = task_name
        self.field_mapping, self.metrics = SettingsYAML.get_instance().get_evaluation_field_mapping_and_metrics(task_id)
        pass

    def evaluate(self, resource_entries):
        evaluation_results = {}
        for correct_value_field_name, predicted_value_field_name in self.field_mapping.items():
            correct_values = []
            predicted_values = []
            for resource_entry in resource_entries:
                correct_values.append(resource_entry.get_value(correct_value_field_name))
                predicted_values.append(resource_entry.get_value(predicted_value_field_name))

            # TO-DO: Check if f1 score should be evaluated
            f1_score = self.evaluate_f1_score(correct_values, predicted_values)
            if f1_score is not None:
                evaluation_results['f1_score'] = f1_score
        return evaluation_results

    def evaluate_f1_score(self, correct_values, predicted_values):
        average = 'micro'

        if 'f1_score' in self.metrics:
            average = self.metrics['f1_score']['average']
            score = f1_score(correct_values, predicted_values, average=average)
            return score

        return None