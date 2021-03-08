from nltk.corpus import stopwords
import logging
import nltk


class QuestionProcessingParser:
    question_processing_settings = None

    def __init__(self, settings):
        self.question_processing_settings = settings

    def parse_question(self, question):
        if str.upper(self.question_processing_settings['parsingTechnique']) == 'SIMPLESPLIT':
            self.__technique_simple_split(question)
        else:
            logging.warning('Technique ' + self.question_processing_settings['parsingTechnique'] + ' not implemented')

        return question

    def __technique_simple_split(self, question):
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')  # downloads only once

        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords')  # downloads only once

        stop_words = set(stopwords.words('english'))

        question_text = question.get_text()
        try:
            tokens = nltk.word_tokenize(question_text)  # generate tokens
        except Exception as e:
            logging.error(str(e))
            raise

        filtered_sentence = [w for w in tokens if not w in stop_words]  # O(n)
        question.set_query(filtered_sentence)
        pass
