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
            with open("./config/pipeline_configuration.json") as json_data_file:
                cls._configuration_file = json.load(json_data_file)
        return cls._instance

    @classmethod
    def get_all_dataset_names(cls):
        dataset_names = []
        datasets = cls._configuration_file['datasets']
        for dataset in datasets:
            dataset_names.append(dataset['name'])
        return dataset_names

    @staticmethod
    def determine_reader_type(reader_type):
        if reader_type == 'WikiPassageQA':
            return ImplementedDatasetReaders.DatasetWikiPassageQA
        elif reader_type == 'QAChave':
            return ImplementedDatasetReaders.DatasetQAChave
        return ImplementedDatasetReaders.DatasetUnknown

    @classmethod
    def get_dataset_reader_type(cls, dataset_name):
        datasets = cls._configuration_file['datasets']
        reader_type = ''
        for dataset in datasets:
            if dataset['name'] == dataset_name:
                return cls.determine_reader_type(dataset['reader_type'])

        return cls.determine_reader_type('')

    @classmethod
    def get_dataset_path(cls, dataset_name):
        datasets = cls._configuration_file['datasets']
        for dataset in datasets:
            if dataset['name'] == dataset_name:
                return dataset['path']

        return ''

    @classmethod
    def get_field_mapping(cls, dataset_name):
        field_mapping = {}
        tasks = cls._configuration_file['pipeline']['tasks']
        for task in tasks:
            used_datasets = task['used_datasets']
            for used_dataset in used_datasets:
                if used_dataset['name'] == dataset_name:
                    input_fields = used_dataset['input_fields']
                    for field, mapped_value in input_fields.items():
                        field_mapping[field] = mapped_value

        return field_mapping

    @classmethod
    def get_expected_datasets(cls, task_id):
        """
        Returns all datasets that are configured to be parsed by the task.
        :return: List with all dataset names.
        """
        datasets_used_in_task = set()
        tasks = cls._configuration_file['pipeline']['tasks']
        for task in tasks:
            if task['id'] == task_id:
                used_datasets = task['used_datasets']
                for used_dataset in used_datasets:
                    datasets_used_in_task.add(used_dataset['name'])

        return list(datasets_used_in_task)

    @classmethod
    def get_fields_to_map_task_result(cls, task_id):
        """
        Get all field names where the task result is supposed to be mapped.
        :return: List with all field names.
        """
        fields_to_map = set()

        tasks = cls._configuration_file['pipeline']['tasks']
        for task in tasks:
            used_datasets = task['used_datasets']
            for used_dataset in used_datasets:
                input_fields = used_dataset['input_fields']
                for field, mapped_value in input_fields.items():
                    try:
                        mapped_task_id = int(mapped_value.split('_')[2])
                    except (IndexError, ValueError):
                        mapped_task_id = -1

                    if mapped_task_id == task_id:
                        fields_to_map.add(field)
        return list(fields_to_map)

    @classmethod
    def get_set_usage(cls, task_id):
        tasks = cls._configuration_file['pipeline']['tasks']
        predict_train = False
        predict_dev = False
        predict_test = False
        for task in tasks:
            if task['id'] == task_id:
                predicts = task['predicts']
                if ('predict_train' in predicts) and (predicts['predict_train']):
                    predict_train = True
                if ('predict_dev' in predicts) and (predicts['predict_dev']):
                    predict_dev = True
                if ('predict_test' in predicts) and (predicts['predict_test']):
                    predict_test = True

        return predict_train, predict_dev, predict_test

    @classmethod
    def get_used_technique(cls, task_id):
        tasks = cls._configuration_file['pipeline']['tasks']
        for task in tasks:
            if task['id'] == task_id:
                return task['technique']

    @classmethod
    def tasks_to_create(cls):
        """
        :return: list with the basic information to create the required tasks.
        """
        tasks_to_created = {}
        tasks = cls._configuration_file['pipeline']['tasks']
        for task in tasks:
            if 'ignore' in task:
                should_ignore = task['ignore']
            else:
                should_ignore = False
            tasks_to_created[task['id']] = {
                "name": task['name'],
                "ignore": should_ignore
            }

        return tasks_to_created
