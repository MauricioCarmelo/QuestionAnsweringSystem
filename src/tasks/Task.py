import abc

class Task:

    def __init__(self):
        self.technique = None

    @abc.abstractmethod
    def execute(self, train_questions, dev_questions, test_questions):
        ...

    @abc.abstractmethod
    def evaluate(self, predicted_data, correct_data):
        ...