from Technique import Technique
import nltk
from nltk.corpus import stopwords


class TechniqueNLTKTokenizerWithoutStopWords(Technique):

    def run(self, resource_entries):
        results = []
        for resource_entry in resource_entries:
            result = self.__run_technique(resource_entry)
            results.append(result)
        return results

    def __run_technique(self, resource_entry):
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')  # downloads only once

        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords')  # downloads only once

        stop_words = set(stopwords.words('english'))
        question_text = resource_entry.get_value('question')

        try:
            if (question_text is not None) and (len(question_text) > 0):
                tokens = nltk.word_tokenize(question_text)  # generate tokens
            else:
                tokens = []
        except Exception as e:
            print(str(e))
            raise

        filtered_sentence = [w for w in tokens if not w in stop_words]  # O(n)

        return filtered_sentence
