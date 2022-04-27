from src.tasks.Technique import Technique
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy
import nltk
from nltk.corpus import stopwords


class TechniqueLinearSVCQuestionClassification(Technique):

    def run(self, resource_entries):
        results = []
        for resource_entry in resource_entries:
            result = self.__run_technique(resource_entry)
            results.append(result)
        return results

    def __run_technique(self, resource_entry):
        question_text = str(resource_entry.get_value(self.get_actual_field_name('question')))
        predicted_value = self.model.predict(self.vectorizer.transform([question_text]))
        return predicted_value[0]

    def setup(self):
        self.model = LinearSVC()
        self.vectorizer = TfidfVectorizer()

        self.stop_words = set(stopwords.words('portuguese'))

    def train(self, train_set, dev_set, test_set, resource_articles):
        question_texts = []
        answer_types = []

        for entry in train_set:
            question_text = entry.get_value(self.get_actual_field_name('question'))

            try:
                if (question_text is not None) and (len(question_text) > 0):
                    tokens = nltk.word_tokenize(question_text)  # generate tokens
                else:
                    tokens = []
            except Exception as e:
                print(str(e))
                raise

            question_text = [w for w in tokens if not w in self.stop_words]

            answer_type = entry.get_value('answer_type')
            if question_text is not None:
                question_texts.append(' '.join(question_text))
                answer_types.append(answer_type)

        x = self.vectorizer.fit_transform(question_texts)
        y = numpy.array(answer_types)
        self.model.fit(x, y)

    def validate(self, dev_set):
        pass
