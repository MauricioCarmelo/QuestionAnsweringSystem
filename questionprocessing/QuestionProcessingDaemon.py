from questionprocessing.WikiPassageQADatasetController import WikiPassageQADatasetController
from questionprocessing.QuestionProcessingParser import QuestionProcessingParser
import logging


class QuestionProcessingDaemon:
    settings = {}
    dataset_controller = None
    question_parser = None

    def __init__(self, question_processing_settings):
        self.settings = question_processing_settings

    def __build_dataset_controller(self):
        try:
            if str.upper(self.settings['dataset']['name']) == 'WIKIPASSAGEQA':
                self.dataset_controller = WikiPassageQADatasetController(self.settings)
        except Exception as e:
            logging.error(str(e))
            raise

    def __build_question_parser(self):
        self.question_parser = QuestionProcessingParser(self.settings)

    def execute(self):
        try:
            self.__build_dataset_controller()
            questions = self.dataset_controller.load_all_questions()
            if len(questions) > 0:  # if any question were loaded from the dataset
                self.dataset_controller.set_questions(questions)
                self.__build_question_parser()

                # apply parsing technique to all questions
                for question in self.dataset_controller.get_questions():
                    self.question_parser.parse_question(question)
            else:
                logging.info('No questions were read from the dataset')
        except Exception as e:
            logging.error(str(e))
            raise
