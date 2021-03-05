from questionprocessing.WikiPassageQADatasetController import WikiPassageQADatasetController
import logging


class QuestionProcessingDaemon:
    settings = {}
    dataset_controller = None

    def __init__(self, question_processing_settings):
        self.settings = question_processing_settings

    def __build_dataset_controller(self):
        try:
            if str.upper(self.settings['dataset']['name']) == 'WIKIPASSAGEQA':
                self.dataset_controller = WikiPassageQADatasetController(self.settings)
        except Exception as e:
            logging.error(str(e))
            raise

    def run(self):
        try:
            self.__build_dataset_controller()
            if self.dataset_controller.load_all_questions():
                pass # continue from here
            else:
                logging.info('No questions were read from the dataset')
        except Exception as e:
            logging.error(str(e))
            raise
