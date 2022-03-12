from src.ResourceEntry import ResourceEntry
from src.SettingsYAML import SettingsYAML
from src.Generator import Generator
from src.datasetreader.BuilderDatasetReader import BuilderDatasetReader


class Resource:
    def __init__(self, dataset_name, dataset_reader_type):
        self.dataset_name = dataset_name
        self.dataset_reader_type = dataset_reader_type
        self.dataset_reader = None
        self.field_mapping = SettingsYAML.get_instance().get_field_mapping(dataset_name)
        self.result_fields = SettingsYAML.get_instance().get_tasks_result_field()

        self.generator = Generator()
        self.resource_entries = []
        self.articles = {}
        # self.resource_entries_train = []
        # self.resource_entries_dev = []
        # self.resource_entries_test = []

    def get_dataset_reader_type(self):
        return self.dataset_reader_type

    def get_dataset_name(self):
        return self.dataset_name

    def get_resource_entries(self):
        return self.resource_entries

    def get_articles(self):
        return self.articles
    # def get_train_entries(self):
    #     return self.resource_entries_train
    #
    # def get_dev_entries(self):
    #     return self.resource_entries_dev
    #
    # def get_test_entries(self):
    #     return self.resource_entries_test

    def __field_key_from_value(self, v):
        for key, value in self.field_mapping.items():
            if v == value:
                return key

    def __get_dataset_fields(self):
        """
        Get the mapping from self.field_mapping of all keys that start with 'dataset_'.
        :return: list with the name of the fields specific to the dataset.
        """
        dataset_specific_fields = []
        for field, specific_field in self.field_mapping.items():
            if field.startswith('dataset_'):
                dataset_specific_fields.append(specific_field)

        return dataset_specific_fields

    def build_resource_entries(self):
        """
        Builds resource entry objects according to the information that was read from the dataset.
        """
        self.dataset_reader = BuilderDatasetReader.build_dataset_reader(self.dataset_name, self.dataset_reader_type)
        if self.dataset_reader is not None:
            entries = self.dataset_reader.load_entries()
            self.filter(entries)
            for resource_entry in entries:
                # Add result fields to the resource entry
                resource_entry.add_fields(self.result_fields)
                self.resource_entries.append(resource_entry)

    def load_articles(self):
        self.articles = self.dataset_reader.load_articles()

    def filter(self, entries):
        filter_fields = SettingsYAML.get_dataset_filter_fields(self.dataset_name)
        for i in range(len(entries)-1):
            if i < len(entries):
                resource_entry_value_mapping = entries[i].get_field_value_mapping()
                for filter_field, value in filter_fields.items():
                    if filter_field in resource_entry_value_mapping and value == resource_entry_value_mapping[filter_field]:
                        entries.pop(i)
                        break
