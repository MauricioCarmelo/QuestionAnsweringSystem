from questionprocessing.DatasetController import DatasetController
import pandas as pd
import logging
from collections import deque
from questionprocessing.Question import Question


class WikiPassageQADatasetController(DatasetController):
    # questions objects are indexed in the dictionary by the identification parameter
    questions = deque()

    def get_question_metadata_parameters(self):
        return ['QID', 'Question', 'DocumentID', 'DocumentName', 'RelevantPassages']

    def get_question_text_parameter(self):
        return 'Question'

    def load_all_questions(self, questions = deque()):
        try:
            path = self.question_processing_settings['dataset']['path']
            data = pd.read_csv(path + 'dev.tsv', sep='\t')

            count_row = data.shape[0]
            count_col = data.shape[1]
            logging.info("Reading dataset from file. Rows = " + str(count_row) + " Columns = " + str(count_col))

            for index, row in data.iterrows():
                # creates an object to type Question
                question = Question(self.question_metadata_parameters)
                # Add all metadata values of the question in the question object
                for parameter in self.question_metadata_parameters:

                    value = row[parameter]
                    if parameter == self.question_text_parameter:
                        question.set_text(value)
                    else:
                        question.insert_metadata_value(parameter, value)

                questions.appendleft(question)

            # stores a reference of the queue in an attribute of DatasetController
            self.questions = questions
            if len(questions) > 0:
                return True
            return False
        except Exception as e:
            logging.error(str(e))
            return False
