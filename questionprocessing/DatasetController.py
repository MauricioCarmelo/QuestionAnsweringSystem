import abc
from collections import deque


class DatasetController(metaclass=abc.ABCMeta):
    question_processing_settings = None
    question_metadata_parameters = []
    question_text_parameter = ''
    questions = None

    def __init__(self, settings):
        self.question_processing_settings = settings
        self.question_metadata_parameters = self.get_question_metadata_parameters()
        self.question_text_parameter = self.get_question_text_parameter()

    def get_questions(self):
        return self.questions

    """
        This method is intended to load the dataset and create an instance of Question for every question 
        in the dataset.
        Returns True if any questions were read from the dataset, False otherwise.
    """
    @abc.abstractmethod
    def load_all_questions(self, questions = deque()):
        pass

    """
       Use this method to define the metadata parameters. These parameters are specific of each dataset
    """
    @abc.abstractmethod
    def get_question_metadata_parameters(self):
        pass

    """
        Use this method to define the parameter used to identify a question.
    """
    @abc.abstractmethod
    def get_question_text_parameter(self):
        pass
