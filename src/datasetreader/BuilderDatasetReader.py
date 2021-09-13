from src.Settings import Settings
from src.NewSettings import NewSettings
from src.datasetreader.ImplementedDatasetReaders import ImplementedDatasetReaders
from src.datasetreader.DatasetReaderWikiPassageQA import DatasetReaderWikiPassageQA
from src.datasetreader.DatasetReaderQAChave import DatasetReaderQAChave


class BuilderDatasetReader:

    @staticmethod
    def build_dataset_reader(dataset_name, dataset_reader_type):
        """
        Builds the dataset reader according to the dataset type.
        :return: dataset_reader (DatasetReader).
        """
        dataset_path = NewSettings.get_instance().get_dataset_path(dataset_name)

        # Create dataset reader object.
        if dataset_reader_type == ImplementedDatasetReaders.DatasetWikiPassageQA:
            dataset_reader = DatasetReaderWikiPassageQA(dataset_name, dataset_path)
        elif dataset_reader_type == ImplementedDatasetReaders.DatasetQAChave:
            dataset_reader = DatasetReaderQAChave(dataset_name, dataset_path)
        else:
            dataset_reader = None

        return dataset_reader
