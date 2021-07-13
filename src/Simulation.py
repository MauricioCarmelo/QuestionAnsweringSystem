from src.Settings import Settings
from Resource import Resource
from Pipeline import Pipeline
from src.tasks.TaskGenerateQuery import TaskGenerateQuery
from src.tasks.TaskAnswerTypeClassification import TaskAnswerTypeClassification


class Simulation:
    def __init__(self):
        self.used_datasets = Settings.get_instance().get_all_used_dataset_names()

    def __build_task(self, task_id, task_name):
        if task_name == 'generate_query':
            return TaskGenerateQuery(task_id, task_name)
        elif task_name == 'answer_type_classification':
            return TaskAnswerTypeClassification(task_id, task_name)
        else:
            return None

    def build_tasks(self):
        created_tasks = []
        tasks_to_create = Settings.get_instance().tasks_to_create()

        ids = list(tasks_to_create.keys())
        ids.sort()  # Sort id list to make sure the tasks are created in the correct sequence.
        for task_id in ids:
            task_parameters = tasks_to_create[task_id]
            if 'ignore' in task_parameters and task_parameters['ignore']:
                pass
            else:
                created_task = self.__build_task(task_id, task_parameters['name'])
                created_tasks.append(created_task)

        return created_tasks

    def run(self):
        for dataset_name in self.used_datasets:
            pipeline = Pipeline()

            # Create, build, and add the resource to the pipeline
            reader_type = Settings.get_instance().get_dataset_reader_type(dataset_name)
            resource = Resource(dataset_name, reader_type)

            resource.build_resource_entries()
            pipeline.set_resource(resource)

            # Create and add the required tasks to the pipeline
            tasks = self.build_tasks()
            for task in tasks:
                if task is not None:
                    task_input_field_mapping = Settings.get_instance().get_task_input_field_mapping(task.get_id(), dataset_name)
                    task.set_input_field_mapping(task_input_field_mapping)
                    pipeline.add_task(task)

            # Run the pipeline
            pipeline.run()
            pass
