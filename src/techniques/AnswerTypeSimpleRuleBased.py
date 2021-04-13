from src.techniques.Technique import Technique


class AnswerTypeSimpleRuleBased(Technique):

    def __init__(self):
        super(AnswerTypeSimpleRuleBased, self).__init__()

    def execute(self, train_questions, dev_questions, test_questions):
        ret = []
        for question in test_questions:
            ret.append(self._answer_type_rules(question["question"]))
        return ret

    def _answer_type_rules(self, question_text):
        if question_text is None:
            return "OTHER"
        question_text = question_text.replace("\n", "")
        tokens = question_text.split(" ")
        if tokens[0].lower() == "quem":
            return "PERSON"
        elif tokens[0].lower() == "onde":
            return "LOCATION"
        elif tokens[0].lower() == "que":
            return "OBJECT"
        elif tokens[0].lower() == "quantos":
            return "MEASURE"
        elif tokens[0].lower() == "como":
            return "MANNER"
        else:
            return "OTHER"