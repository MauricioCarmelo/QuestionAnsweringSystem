from src.tasks.Task import Task


class TaskGenerateQuery(Task):
    @staticmethod
    def get_fields_for_technique():
        return []

    def run(self, resource_entries):
        technique = super().build_technique()
        return technique.run(resource_entries)
