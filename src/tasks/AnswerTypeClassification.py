from src.tasks.Task import Task
from sklearn.metrics import f1_score
import numpy as np


class AnswerTypeClassification(Task):

    def __init__(self):
        super(AnswerTypeClassification, self).__init__()

    def execute(self, train_questions, dev_questions, test_questions):
        pridicted_data = self.technique.execute(train_questions, dev_questions, test_questions)
        results = self.evaluate(test_questions, pridicted_data)
        return results

    def evaluate(self, true_data, predicted_data):
        _true_data = np.array([v["answer_type"] for v in true_data])
        ret = {"f1-macro": f1_score(_true_data, np.array(predicted_data), average='macro'),
               "f1-micro": f1_score(_true_data, np.array(predicted_data), average='micro')}
        return ret
