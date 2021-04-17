from src.Settings import Settings
import logging

class Pipeline:
    def __init__(self):
        self.tasks = []
        self.resources = []

    def add_task(self, task):
        if task is not None:
            self.tasks.append(task)

    def add_resource(self, resource):
        if resource is not None:
            self.resources.append(resource)

    def run_tasks(self):
        try:
            for task in self.tasks:
                fields_to_map_task_result = Settings.get_instance().get_mapped_fields(task.get_id())

                # Get the dataset reader types that are configured for the task
                expected_datasets = set()
                for expected_dataset_name in Settings.get_instance().get_expected_datasets(task.get_id()):
                    expected_datasets.add(Settings.get_instance().get_dataset_reader_type(expected_dataset_name))

                for resource in self.resources:
                    if resource.get_dataset_reader_type() in expected_datasets:
                        resource_entries = resource.get_resource_entries()

                        # Run the task for all resource entries
                        for resource_entry in resource_entries:
                            task.validate_resource_entry(resource_entry)
                            task_result = task.run_technique(resource_entry)
                            # Insert the generated result in all fields of the resource entry that expect the value.
                            for field in fields_to_map_task_result:
                                resource_entry.add_mapped_value(field, task_result)
        except Exception as e:
            logging.error(str(e))