from src.Settings import Settings
from src.tasks.TaskGenerateQuery import TaskGenerateQuery
from src.tasks.TechniqueNLTKTokenizerWithoutStopWords import TechniqueNLTKTokenizerWithoutStopWords


class Utils:
    @staticmethod
    def build_tasks():
        created_tasks = []
        tasks_to_create = Settings.get_instance().tasks_to_create()

        ids = list(tasks_to_create.keys())
        ids.sort()  # Sort id list to make sure the tasks are created in the correct sequence.
        for task_id in ids:
            task_info = tasks_to_create[task_id]
            if 'ignore' in task_info and task_info['ignore']:
                pass
            else:
                created_task = Utils.__build_task(task_id, task_info)
                created_tasks.append(created_task)

        return created_tasks

    @staticmethod
    def __build_task(task_id, task_info):
        name = task_info['name']

        if name == 'generate_query':
            return TaskGenerateQuery(task_id)
        else:
            return None

    @staticmethod
    def build_technique(task_id):
        if Settings.get_instance().get_used_technique(task_id) == 'nltkTokenizerWithoutStopWords':
            return TechniqueNLTKTokenizerWithoutStopWords('nltkTokenizerWithoutStopWords')
        else:
            return None
