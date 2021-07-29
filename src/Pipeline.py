from src.Settings import Settings
from src.Generator import Generator
from src.evaluation.Evaluator import Evaluator


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
        self.__run_pipeline(self.resource.get_dataset_name())

    # def build_evaluator(self, dataset_name, task_id, task_name):
        # Get the evaluation type and create the evaluator
        # evaluator_type = Settings.get_instance().get_evaluator_type_for_task(task_id)

        # if evaluator_type == 'ValueComparison':
        #    return EvaluatorValueComparison(dataset_name, task_id, task_name)
        # else:
        #    return None

    def __run_pipeline(self, dataset_name):
        # Build a generator according to the configuration of the dataset in the current task.
        generator = Generator.cycles_generator(self.resource.get_resource_entries(), dataset_name)

        for train_set, dev_set, test_set in generator:

            for task in self.tasks:
                # fields_to_map_task_result = Settings.get_instance().get_fields_to_map_task_result(task.get_id())
                field_to_map_task_result = 'result_task_' + str(task.get_id())

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
                            # for field in fields_to_map_task_result:
                            #     resource_entry.add_mapped_value(field, task_result)
                            resource_entry.add_mapped_value(field_to_map_task_result, task_result)

                    if predict_dev:
                        # Run task for predict set
                        task_generated_results = task.run(dev_set)
                        for task_result, resource_entry in zip(task_generated_results, dev_set):
                            # Insert the task result in the result entry for all fields that are expecting the value
                            # for field in fields_to_map_task_result:
                            #     resource_entry.add_mapped_value(field, task_result)
                            resource_entry.add_mapped_value(field_to_map_task_result, task_result)

                    if predict_test:
                        # Run task for test set
                        task_generated_results = task.run(test_set)
                        for task_result, resource_entry in zip(task_generated_results, test_set):
                            # Insert the task result in the result entry for all fields that are expecting the value
                            # for field in fields_to_map_task_result:
                            #     resource_entry.add_mapped_value(field, task_result)
                            resource_entry.add_mapped_value(field_to_map_task_result, task_result)

                    # Evaluation steps
                    if task.should_evaluate():
                        # evaluator = self.build_evaluator(dataset_name, task.get_id(), task.get_name())
                        evaluator = Evaluator(dataset_name, task.get_id(), task.get_name())

                        # Get which sets are supposed to be evaluated
                        evaluate_train, evaluate_dev, evaluate_test = \
                            Settings.get_instance().get_set_usage_for_evaluation(task.get_id())

                        if evaluate_train:
                            evaluator.evaluate(train_set)
                        if evaluate_dev:
                            evaluator.evaluate(dev_set)
                        if evaluate_test:
                            evaluator.evaluate(test_set)
