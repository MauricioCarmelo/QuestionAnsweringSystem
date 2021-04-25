from src.datasetreader.ImplementedDatasetReaders import ImplementedDatasetReaders
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
            with open("./config/step2_pipeline.json") as json_data_file:
                cls._configuration_file = json.load(json_data_file)
        return cls._instance

    def is_valid(self):
        return True

    @staticmethod
    def get_all_dataset_names():
        return ['WikiPassageQA', 'QAChave']

    @staticmethod
    def get_dataset_reader_type(dataset_name):
        if dataset_name == 'WikiPassageQA':
            return ImplementedDatasetReaders.DatasetWikiPassageQA
        elif dataset_name == 'QAChave':
            return ImplementedDatasetReaders.DatasetQAChave
        return None

    @staticmethod
    def get_dataset_path(dataset_name):
        if dataset_name == 'WikiPassageQA':
            return './datasets/WikiPassageQA/'
        elif dataset_name == 'QAChave':
            return './datasets/qa-chave'
        else:
            return ''

    @staticmethod
    def get_field_mapping(dataset_name):
        return {'query': 'result_task0',
                'list_of_documents': 'result_task1'}

    @staticmethod
    def get_dataset_input_fields(dataset_name):
        return None

    @staticmethod
    def get_expected_datasets(task_id):
        """
        Returns all datasets that are configured to be parsed by the task.
        :return: List with all dataset names.
        """
        if task_id == 0:
            return ['WikiPassageQA', 'QAChave']
        return None

    @staticmethod
    def get_mapped_fields(task_id):
        """
        Get all field names where the task result is supposed to be mapped.
        :return: List with all field names.
        """
        task_result_name = 'result_task' + str(task_id)

        # this is a test
        if task_result_name == 'result_task0':
            return ['query']
        elif task_result_name == 'result_task1':
            return ['list_of_documents']
        return []

    @staticmethod
    def get_set_usage(task_id):
        return True, True, True

    @staticmethod
    def get_used_technique(task_id):
        return 'nltkTokenizerWithoutStopWords'
