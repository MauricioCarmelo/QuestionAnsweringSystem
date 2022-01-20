from src.datasetreader.ImplementedDatasetReaders import ImplementedDatasetReaders
import yaml


class SettingsYAML:
    _instance = None
    _configured_datasets = None
    _configured_tasks = None

    def __init__(self):
        raise RuntimeError()

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)

            datasets_file = open("./config/datasets.yaml")
            parsed_datasets_file = yaml.load_all(datasets_file, Loader=yaml.FullLoader)
            cls._configured_datasets = []
            for dataset in parsed_datasets_file:
                cls._configured_datasets.append(dataset['dataset'])

            pipeline_file = open("./config/pipeline.yaml")
            parsed_pipeline_file = yaml.load_all(pipeline_file, Loader=yaml.FullLoader)
            cls._configured_tasks = []
            for task in parsed_pipeline_file:
                cls._configured_tasks.append(task['task'])

        return cls._instance

    @classmethod
    def get_all_dataset_names(cls):
        pass

    @classmethod
    def get_all_used_dataset_names(cls):
        """
        Returns all datasets that are used in at least one task in the pipeline.
        :return: List with all datasets.
        """
        used_dataset_names = set()
        for task in cls._configured_tasks:
            used_datasets = task['used_datasets']
            for used_dataset in used_datasets:
                used_dataset_names.add(used_dataset['used_dataset']['name'])
        return list(used_dataset_names)

    @staticmethod
    def determine_reader_type(reader_type):
        if reader_type == 'WikiPassageQA':
            return ImplementedDatasetReaders.WikiPassageQA
        elif reader_type == 'QAChave':
            return ImplementedDatasetReaders.QAChave
        elif reader_type == 'Antique':
            return ImplementedDatasetReaders.Antique
        elif reader_type == 'UIUC':
            return ImplementedDatasetReaders.UIUC
        return ImplementedDatasetReaders.DatasetUnknown

    @classmethod
    def get_dataset_reader_type(cls, dataset_name):
        for dataset in cls._configured_datasets:
            if dataset['name'] == dataset_name:
                return cls.determine_reader_type(dataset['reader_type'])
        return cls.determine_reader_type('')

    @classmethod
    def get_dataset_path(cls, dataset_name):
        for dataset in cls._configured_datasets:
            if dataset['name'] == dataset_name:
                return dataset['path']
        return ''

    @classmethod
    def get_field_mapping(cls, dataset_name):
        field_mapping = {}
        for task in cls._configured_tasks:
            used_datasets = task['used_datasets']
            for dataset_item in used_datasets:
                if dataset_item['used_dataset']['name'] == dataset_name:
                    input_fields = dataset_item['used_dataset']['input_fields']
                    if not input_fields is None:
                        for field, mapped_value in input_fields.items():
                            field_mapping[field] = mapped_value
        return field_mapping

    @classmethod
    def get_tasks_result_field(cls):
        """
        Get the name of all generated results. Each of these values will be used a key in
        the resource entry dictionary.
        :return: List with the field names.
        """
        result_fields = []
        for task in cls._configured_tasks:
            result_fields.append(task['generated_result'])
        return result_fields

    @classmethod
    def get_task_input_field_mapping(cls, task_id, dataset_name):
        field_mapping = {}
        for task in cls._configured_tasks:
            if task['id'] == task_id:
                used_datasets = task['used_datasets']
                for dataset_item in used_datasets:
                    if dataset_item['used_dataset']['name'] == dataset_name:
                        input_fields = dataset_item['used_dataset']['input_fields']
                        if input_fields is not None:
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
        for task in cls._configured_tasks:
            if task['id'] == task_id:
                used_datasets = task['used_datasets']
                for dataset_item in used_datasets:
                    datasets_used_in_task.add(dataset_item['used_dataset']['name'])

        return list(datasets_used_in_task)

    @classmethod
    def get_fields_to_map_task_result(cls, task_id):
        """
        Get all field names where the task result is supposed to be mapped.
        :return: List with all field names.
        """
        pass

    @classmethod
    def get_set_usage(cls, task_id):
        predict_train = False
        predict_dev = False
        predict_test = False
        for task in cls._configured_tasks:
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
    def get_set_usage_for_evaluation(cls, task_id):
        evaluate_train = False
        evaluate_dev = False
        evaluate_test = False
        for task in cls._configured_tasks:
            if task['id'] == task_id:
                set_usage = task['evaluation']['set_usage']
                if ('evaluate_train' in set_usage) and (set_usage['evaluate_train']):
                    evaluate_train = True
                if ('evaluate_dev' in set_usage) and (set_usage['evaluate_dev']):
                    evaluate_dev = True
                if ('evaluate_test' in set_usage) and (set_usage['evaluate_test']):
                    evaluate_test = True
        return evaluate_train, evaluate_dev, evaluate_test

    @classmethod
    def get_used_technique(cls, task_id):
        for task in cls._configured_tasks:
            if task['id'] == task_id:
                return task['technique']

    @classmethod
    def tasks_to_create(cls):
        """
        :return: list with the basic information to create the required tasks.
        """
        tasks_to_create = {}
        for task in cls._configured_tasks:
            if 'ignore' in task:
                should_ignore = task['ignore']
            else:
                should_ignore = False
            tasks_to_create[task['id']] = {
                "name": task['name'],
                "ignore": should_ignore
            }
        return tasks_to_create

    @classmethod
    def get_evaluator_type_for_task(cls, task_id):
        pass

    @classmethod
    def should_evaluate(cls, task_id):
        for task in cls._configured_tasks:
            if task['id'] == task_id:
                if 'evaluation' in task:
                    evaluation = task['evaluation']
                    if 'should_evaluate' in evaluation and evaluation['should_evaluate']:
                        return True
                    else:
                        return False
        return False

    @classmethod
    def get_setup_settings(cls, dataset_name):
        """
        Get the information that will be used to setup the Generator.
        :param dataset_name: name of the dataset.
        :return: Dictionary with the necessary information.
        """
        evaluation_settings = {}
        # Default values
        evaluation_settings['type'] = ''
        evaluation_settings['folds_splitter'] = ''
        evaluation_settings['folds'] = 10
        evaluation_settings['test_size'] = 0.3
        evaluation_settings['random_state'] = 0

        for dataset in cls._configured_datasets:
            if dataset['name'] == dataset_name and 'dataset_setup' in dataset:
                for key, value in dataset['dataset_setup'].items():
                    evaluation_settings[key] = value
                return evaluation_settings
        return evaluation_settings

    @classmethod
    def get_evaluation_settings(cls, task_id):
        evaluation_settings = None
        for task in cls._configured_tasks:
            if task['id'] == task_id:
                if 'evaluation' in task:
                    evaluation_settings = task['evaluation']

        return evaluation_settings

    @classmethod
    def get_evaluation_field_mapping_and_metrics(cls, task_id):
        field_mapping = {}
        metrics = {}
        evaluation_settings = cls.get_evaluation_settings(task_id)
        if evaluation_settings and 'fields' in evaluation_settings:
            evaluation_fields = evaluation_settings['fields']
            for field, mapped_value in evaluation_fields.items():
                field_mapping[field] = mapped_value

        if evaluation_settings and 'metrics' in evaluation_settings:
            metrics = evaluation_settings['metrics']

        return field_mapping, metrics

    @classmethod
    def get_dataset_filter_fields(cls, dataset_name):
        filter_mapping = {}
        for dataset in cls._configured_datasets:
            if dataset['name'] == dataset_name and 'filter' in dataset:
                for key, value in dataset['filter'].items():
                    filter_mapping[key] = value
                return filter_mapping
        return filter_mapping
