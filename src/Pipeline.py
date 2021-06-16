from src.Settings import Settings
from src.evaluation.EvaluatorDocumentComparison import EvaluatorDocumentComparison


class Pipeline:
    def __init__(self):
        self.tasks = []
        self.resource = None

    def add_task(self, task):
        if task is not None:
            self.tasks.append(task)

    def set_resource(self, resource):
        if resource is not None:
            self.resource = resource

    def run(self):
        self.__run_pipeline(self.resource.get_train_entries(),
                            self.resource.get_dev_entries(),
                            self.resource.get_test_entries(),
                            self.resource.get_dataset_name())

    def build_evaluator(self, dataset_name, task_id, task_name, evaluator_type):
        if evaluator_type == 'DocumentComparison':
            return EvaluatorDocumentComparison(dataset_name, task_id, task_name)
        else:
            return None

    def __run_pipeline(self, train_set, dev_set, test_set, dataset_name):

        for task in self.tasks:
            fields_to_map_task_result = Settings.get_instance().get_fields_to_map_task_result(task.get_id())

            # Get the dataset names that are configured to be run by the task
            expected_datasets = Settings.get_instance().get_expected_datasets(task.get_id())

            if dataset_name in expected_datasets:
                predict_train, predict_dev, predict_test = \
                    Settings.get_instance().get_set_usage(task.get_id())

                task.train(train_set)
                task.validate(dev_set)

                if predict_train:
                    # Run task for training set
                    task_generated_results = task.run(train_set)
                    for task_result, resource_entry in zip(task_generated_results, train_set):
                        # Insert the task result in the result entry for all fields that are expecting the value
                        for field in fields_to_map_task_result:
                            resource_entry.add_mapped_value(field, task_result)

                if predict_dev:
                    # Run task for predict set
                    task_generated_results = task.run(dev_set)
                    for task_result, resource_entry in zip(task_generated_results, dev_set):
                        # Insert the task result in the result entry for all fields that are expecting the value
                        for field in fields_to_map_task_result:
                            resource_entry.add_mapped_value(field, task_result)

                if predict_test:
                    # Run task for test set
                    task_generated_results = task.run(test_set)
                    for task_result, resource_entry in zip(task_generated_results, test_set):
                        # Insert the task result in the result entry for all fields that are expecting the value
                        for field in fields_to_map_task_result:
                            resource_entry.add_mapped_value(field, task_result)

                # Evaluation steps
                if task.should_evaluate():
                    from src.Utils import EvaluatorUtils

                    # Get the evaluation type and create the evaluator
                    evaluator_type = Settings.get_instance().get_task_evaluator_type()
                    evaluator = self.build_evaluator(dataset_name, task.get_id(), task.get_name(),
                                                               evaluator_type)

                    # Get which sets are supposed to be evaluated
                    evaluate_train, evaluate_dev, evaluate_test = \
                        Settings.get_instance().get_set_usage_for_evaluation(task.get_id())
                    resource_entries_for_evaluation = []

                    if evaluate_train:
                        resource_entries_for_evaluation.extend(train_set)
                    if evaluate_dev:
                        resource_entries_for_evaluation.extend(dev_set)
                    if evaluate_test:
                        resource_entries_for_evaluation.extend(test_set)

                    # Evaluate resource entries
                    evaluator.evaluate_resource_entries(resource_entries_for_evaluation)
