from src.Settings import Settings
from Resource import Resource
from Pipeline import Pipeline
from src.tasks.TaskGenerateQuery import TaskGenerateQuery


class Simulation:
    def __init__(self):
        self.used_datasets = Settings.get_instance().get_all_dataset_names()

    def run(self):
        for dataset_name in self.used_datasets:
            reader_type = Settings.get_instance().get_dataset_reader_type(dataset_name)

            # Passar por cada um dos resources;
            resource = Resource(dataset_name, reader_type)
            resource.build_resource_entries()

            # Substituir pelo task builder e receber uma lista de tasks. Adicionar cada uma dessas tasks ao pipeline.
            task0 = TaskGenerateQuery(0)

            pipeline = Pipeline()
            pipeline.set_resource(resource)
            pipeline.add_task(task0)
            pipeline.run()
            pass
