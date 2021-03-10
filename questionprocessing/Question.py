class Question:
    def __init__(self, parameters, id_parameter, text_parameter):
        self.parameters = parameters
        self.id_parameter = id_parameter
        self.text_parameter = text_parameter
        self.metadata_information = {}
        self.query = None  # result from parse technique

    def get_id(self):
        if self.id_parameter in self.metadata_information:
            return self.metadata_information[self.id_parameter]

    def get_text(self):
        if self.text_parameter in self.metadata_information:
            return self.metadata_information[self.text_parameter]

    def set_query(self, query):
        self.query = query

    def insert_metadata_value(self, parameter, value):
        self.metadata_information[parameter] = value
