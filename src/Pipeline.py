from src.Settings import Settings


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

    def __run_pipeline(self, train_set, dev_set, test_set, dataset_name):

        for task in self.tasks:
            fields_to_map_task_result = Settings.get_instance().get_mapped_fields(task.get_id())

            # Get the dataset reader types that are configured for the task
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