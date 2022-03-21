from src.tasks.Technique import Technique
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy


class TechniqueSVMLinearQuestionClassification(Technique):

    def run(self, resource_entries):
        results = []
        for resource_entry in resource_entries:
            result = self.__run_technique(resource_entry)
            results.append(result)
        return results

    def __run_technique(self, resource_entry):
        question_text = str(resource_entry.get_value('question'))
        predicted_value = self.model.predict(self.vectorizer.transform([question_text]))
        return predicted_value

    def setup(self):
        # Create a svm Classifier
        self.model = svm.SVC(kernel='linear')  # Linear Kernel
        self.vectorizer = TfidfVectorizer()

    def train(self, train_set, dev_set, test_set, resource_articles):
        question_texts = []
        answer_types = []
        for entry in train_set:
            question_text = entry.get_value('question')
            answer_type = entry.get_value('answer_type')
            if question_text is not None:
                question_texts.append(question_text)
                answer_types.append(answer_type)

        # Train the model using the training sets
        x = self.vectorizer.fit_transform(question_texts)
        y = numpy.array(answer_types)
        self.model.fit(x, y)

    def validate(self, dev_set):
        pass
