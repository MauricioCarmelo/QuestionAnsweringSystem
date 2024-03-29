from src.ResourceEntry import ResourceEntry
from src.Settings import Settings
from src.Generator import Generator
from src.datasetreader.BuilderDatasetReader import BuilderDatasetReader
import logging


class Resource:
    def __init__(self, dataset_name, dataset_reader_type):
        self.dataset_name = dataset_name
        self.dataset_reader_type = dataset_reader_type
        self.field_mapping = Settings.get_instance().get_field_mapping(dataset_name)

        self.generator = Generator()
        self.resource_entries_train = []
        self.resource_entries_dev = []
        self.resource_entries_test = []

    def get_dataset_reader_type(self):
        return self.dataset_reader_type

    def get_dataset_name(self):
        return self.dataset_name

    def get_train_entries(self):
        return self.resource_entries_train

    def get_dev_entries(self):
        return self.resource_entries_dev

    def get_test_entries(self):
        return self.resource_entries_test

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
        resource_entries = []

        dataset_reader = BuilderDatasetReader.build_dataset_reader(self.dataset_name, self.dataset_reader_type)
        if dataset_reader is not None:
            entries_from_dataset = dataset_reader.load_entries()

            if entries_from_dataset is not None:
                # For each entry that was read from the dataset
                for entry in entries_from_dataset:
                    # Creates a resource entry.
                    resource_entry = ResourceEntry(self.field_mapping.keys())
                    resource_entry.append_dictionary_values(entry)

                    resource_entries.append(resource_entry)

                    self.resource_entries_train, self.resource_entries_dev, \
                        self.resource_entries_train = self.generator.get_train_dev_test_sets(resource_entries)

            else:
                logging.error("No entry read from dataset")
        else:
            logging.error("Not able to create dataset reader")
