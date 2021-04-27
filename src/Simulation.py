from src.Settings import Settings
from src.tasks.TaskUtils import TaskUtils
from Resource import Resource
from Pipeline import Pipeline



class Simulation:
    def __init__(self):
        self.used_datasets = Settings.get_instance().get_all_dataset_names()

    def run(self):
        for dataset_name in self.used_datasets:
            reader_type = Settings.get_instance().get_dataset_reader_type(dataset_name)

            # Passar por cada um dos resources;
            resource = Resource(dataset_name, reader_type)
            resource.build_resource_entries()

            tasks = TaskUtils.build_tasks()

            pipeline = Pipeline()
            pipeline.set_resource(resource)
            for task in tasks:
                if task is not None:
                    pipeline.add_task(task)

            pipeline.run()
            pass
