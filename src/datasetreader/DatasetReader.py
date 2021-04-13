import abc


class DatasetReader:
    def __init__(self, name=""):
        self.name = name

    @abc.abstractmethod
    def load_entries(self):
        """
        Loads, from the dataset, all the questions and their parameters values.
        :return: list of dictionaries where each item is a question instance with its attributes.
        """
        # ToDo: check if DataFrame is the better data structure. Probably a json format is better due
        #  to the QUESTION_COLUMNS structure.

        pass


# ToDo: Think a better way where to put it to make easy create and understand the possible question fields
# ToDo: maybe it may not be a dictionary with the data type. Perhaps a string list is enough
# It is just to visualize the question values structure. Maybe, we should think a simple structure form.
QUESTION_COLUMNS = {
    "id": None,
    "question": None,
    "question_domain": None,
    "answer_type": None,
    "answers": [{"id": None, "answer": None,
                 "documents": [{"id": None, "name": None, "document": None}],
                 "passages": [{"id": None, "name": None, "passage": None}],
                 "sentences": [{"id": None, "name": None, "sentence": None}]}
                ],
    "entities": [{"entity": None, "start": None, "end": None, "type": None, "subtype": None}],
    "tokens": [],

    # When the collection contains a predefined division of training, dev, and test data,
    # this column determines which group this question belongs to. Possible values: NaN, train, dev, test.
    "pre_evaluation_group": None,

    "evaluation_group": None,
}
