class Question:
    text = ''
    parameters = None
    metadata_information = {}

    def __init__(self, parameters):
        self.parameters = parameters

    def set_text(self, text):
        self.text = text

    def insert_metadata_value(self, parameter, value):
        self.metadata_information[parameter] = value
