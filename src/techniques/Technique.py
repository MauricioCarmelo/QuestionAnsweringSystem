import abc


class Technique:

    def __init__(self):
        self.settings = []

    @abc.abstractmethod
    def execute(self, train_questions, dev_questions, test_questions):
        ...