import json

class Settings:
    _instance = None
    _configuration_file = None

    def __init__(self):
        raise RuntimeError()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            with open("./config/setp2_pipeline.json") as json_data_file:
                cls._configuration_file = json.load(json_data_file)

        return cls._instance

    def is_valid(self):
        return True

    def get_used_datasets(self):
        return None

    def get_dataset_path(self, dataset_name):
        return ''

    def get_all_input_fields(self, dataset_name):
        return None
