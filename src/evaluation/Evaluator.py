import abc
from src.SettingsYAML import SettingsYAML
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score

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

            if 'f1_score' in self.metrics:
                f1_score = self.evaluate_f1_score(correct_values, predicted_values)
                if f1_score is not None:
                    evaluation_results['f1_score'] = f1_score

            if 'precision' in self.metrics:
                precision = self.evaluate_precision(correct_values, predicted_values)
                if precision is not None:
                    evaluation_results['precision'] = precision

            if 'accuracy' in self.metrics:
                accuracy = self.evaluate_accuracy(correct_values, predicted_values)
                if accuracy is not None:
                    evaluation_results['accuracy'] = accuracy

            if 'recall' in self.metrics:
                recall = self.evaluate_recall(correct_values, predicted_values)
                if recall is not None:
                    evaluation_results['recall'] = recall

        return evaluation_results

    def evaluate_f1_score(self, correct_values, predicted_values):
        average = 'micro' # default
        if 'average' in self.metrics['fi_score']:
            average = self.metrics['f1_score']['average']
        score = f1_score(correct_values, predicted_values, average=average)
        return score

    def evaluate_precision(self, correct_values, predicted_values):
        average = 'micro'  # default
        if 'average' in self.metrics['precision']:
            average = self.metrics['precision']['average']
        score = precision_score(correct_values, predicted_values, average=average)
        return score

    def evaluate_accuracy(self, correct_values, predicted_values):
        score = accuracy_score(correct_values, predicted_values)
        return score

    def evaluate_recall(self, correct_values, predicted_values):
        average = 'micro'  # default
        if 'average' in self.metrics['recall']:
            average = self.metrics['recall']['average']
        score = recall_score(correct_values, predicted_values, average=average)
        return score
