from src.datasetreader.ImplementedDatasetReaders import ImplementedDatasetReaders
from src.datasetreader.DatasetReaderWikiPassageQA import DatasetReaderWikiPassageQA
from src.datasetreader.DatasetReaderQAChave import DatasetReaderQAChave
from src.ResourceEntry import ResourceEntry
from src.Settings import Settings
import logging


class Resource:
    def __init__(self, dataset_name, dataset_reader_type):
        self.dataset_name = dataset_name
        self.dataset_reader_type = dataset_reader_type
        self.field_mapping = Settings.get_instance().get_field_mapping(dataset_name)
        self.resource_entries = []

    def get_field_key_from_value(self, v):
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

    def __build_dataset_reader(self):
        """
        Builds the dataset reader according to the dataset type.
        :return: dataset_reader (DatasetReader).
        """
        dataset_path = Settings.get_instance().get_dataset_path(self.dataset_name)
        dataset_fields_to_read = self.__get_dataset_fields()

        # Create dataset reader object.
        if self.dataset_reader_type == ImplementedDatasetReaders.DatasetWikiPassageQA:
            dataset_reader = DatasetReaderWikiPassageQA(self.dataset_name, dataset_path, dataset_fields_to_read)
        elif self.dataset_reader_type == ImplementedDatasetReaders.DatasetQAChave:
            dataset_reader = DatasetReaderQAChave(self.dataset_name, dataset_path, dataset_fields_to_read)
        else:
            logging.error("Dataset type " + self.dataset_reader_type + " not implemented")
            dataset_reader = None

        return dataset_reader

    def build_resource_entries(self):
        """
        Builds resource entry objects according to the information that was read from the dataset.
        """
        dataset_reader = self.__build_dataset_reader()
        if dataset_reader is not None:
            entries_from_dataset = dataset_reader.load_entries()

            if entries_from_dataset is not None:
                # For each entry that was read from the dataset.
                for index, row in entries_from_dataset.iterrows():
                    # Creates a resource entry.
                    resource_entry = ResourceEntry(self.field_mapping.keys())

                    for field in entries_from_dataset.columns.values:
                        # Add the value of the field in the newly created object.
                        resource_entry.add_mapped_value(self.__field_key_from_value(field), row[field])

                    self.resource_entries.append(resource_entry)
            else:
                logging.error("No entry read from dataset")
        else:
            logging.error("Not able to create dataset reader")
