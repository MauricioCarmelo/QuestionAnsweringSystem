from src.tasks.Technique import Technique
import nltk


class TechniqueRuleBased(Technique):

    def run(self, resource_entries):
        results = []
        for resource_entry in resource_entries:
            result = self.__run_technique(resource_entry)
            results.append(result)
        return results

    def __run_technique(self, resource_entry):
        question_text = resource_entry.get_value('question')
        if question_text is None:
            return "OTHER"

        # tokens = question_text.split(" ")
        tokens = nltk.word_tokenize(question_text)  # generate tokens
        first_word = tokens[0].lower()

        if first_word == "quem":
            return "PERSON"
        elif first_word == "onde":
            return "LOCATION"
        elif first_word == "que":
            return "OBJECT"
        elif first_word == "quantos":
            return "MEASURE"
        elif first_word == "como":
            return "MANNER"
        else:
            return "OTHER"
