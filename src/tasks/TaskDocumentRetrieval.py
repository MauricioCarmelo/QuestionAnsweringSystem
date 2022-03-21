from src.tasks.Task import Task


class TaskDocumentRetrieval(Task):
    @staticmethod
    def get_fields_for_technique():
        return []

    def run(self, resource_entries):
        return self._technique.run(resource_entries)
