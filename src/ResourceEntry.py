class ResourceEntry:
    def __init__(self, fields=None):
        self._field_value_mapping = {}
        self._field_value_mapping['id'] = ''
        self._field_value_mapping['question'] = ''
        self._field_value_mapping['question_domain'] = ''
        self._field_value_mapping['answer_type'] = ''
        self._field_value_mapping['answers'] = []
        self._field_value_mapping['entities'] = []
        self._field_value_mapping['tokens'] = []
        self._field_value_mapping['pre_evaluation_group'] = ''
        self._field_value_mapping['evaluation_group'] = ''
        if fields:
            for field in fields:
                self._field_value_mapping[field] = ''
        self._field_value_mapping['indexed_article'] = ''

    def add_fields(self, fields):
        for field in fields:
            self._field_value_mapping[field] = ''

    def set_id(self, id):
        self._field_value_mapping['id'] = id

    def set_question(self, question):
        self._field_value_mapping['question'] = question

    def set_question_domain(self, question_domain):
        self._field_value_mapping['question_domain'] = question_domain

    def set_answer_type(self, answer_type):
        self._field_value_mapping['answer_type'] = answer_type

    def set_evaluation_group(self, evaluation_group):
        self._field_value_mapping['evaluation_group'] = evaluation_group

    def set_pre_evaluation_group(self, pre_evaluation_group):
        self._field_value_mapping['pre_evaluation_group'] = pre_evaluation_group

    def set_indexed_article(self, indexed_article):
        self._field_value_mapping['indexed_article'] = indexed_article

    def add_entity(self, entity, start, end, type, subtype):
        new_entity = {}
        new_entity['entity'] = entity
        new_entity['start'] = start
        new_entity['end'] = end
        new_entity['type'] = type
        new_entity['subtype'] = subtype
        self._field_value_mapping['entities'].append(new_entity)

    def add_token(self, token):
        self._field_value_mapping['tokens'].append(token)

    def add_answer(self, id=0, answer=''):
        new_answer = {}
        new_answer['id'] = id
        new_answer['answer'] = answer
        new_answer['documents'] = []
        new_answer['passages'] = []
        new_answer['sentences'] = []
        self._field_value_mapping['answers'].append(new_answer)

    def _find_answer(self, answer_id):
        for answer in self._field_value_mapping['answers']:
            if answer['id'] == answer_id:
                return answer
        return None

    def add_answer_document(self, answer_id=0, doc_id=0, doc_name='', document=''):
        new_doc = {}
        new_doc['id'] = doc_id
        new_doc['name'] = doc_name
        new_doc['document'] = document
        answer = self._find_answer(answer_id)
        answer['documents'].append(new_doc)

    def add_answer_passages(self, answer_id=0,  passage_id=0, passage_name='', passage=''):
        new_passage = {}
        new_passage['id'] = passage_id
        new_passage['name'] = passage_name
        new_passage['passage'] = passage
        answer = self._find_answer(answer_id)
        answer['passages'].append(new_passage)

    def add_answer_sentences(self, answer_id=0,  sentence_id=0, sentence_name='', sentence=''):
        new_sentece = {}
        new_sentece['id'] = sentence_id
        new_sentece['name'] = sentence_name
        new_sentece['sentence'] = sentence
        answer = self._find_answer(answer_id)
        answer['sentences'].append(new_sentece)

    def get_field_value_mapping(self):
        return self._field_value_mapping

    def get_value(self, field):
        if field in self._field_value_mapping:
            return self._field_value_mapping[field]
        else:
            return None

    def set_value(self, field, value):
        self._field_value_mapping[field] = value

    def add_value(self, field, value):
        self._field_value_mapping[field] = value

    def append_dictionary_values(self, d):
        for key, value in d.items():
            self.add_value(key, value)
