from src.SettingsYAML import SettingsYAML
from src.datasetreader.ImplementedDatasetReaders import ImplementedDatasetReaders
from src.datasetreader.DatasetReaderWikiPassageQA import DatasetReaderWikiPassageQA
from src.datasetreader.DatasetReaderQAChave import DatasetReaderQAChave
from src.datasetreader.DatasetReaderAntique import DatasetReaderAntique
from src.datasetreader.DatasetReaderUIUC import DatasetReaderUIUC
from src.datasetreader.DatasetReaderSQUAD import DatasetReaderSQUAD


class BuilderDatasetReader:

    @staticmethod
    def build_dataset_reader(dataset_name, dataset_reader_type):
        """
        Builds the dataset reader according to the dataset type.
        :return: dataset_reader (DatasetReader).
        """
        dataset_path = SettingsYAML.get_instance().get_dataset_path(dataset_name)

        # Create dataset reader object.
        if dataset_reader_type == ImplementedDatasetReaders.WikiPassageQA:
            dataset_reader = DatasetReaderWikiPassageQA(dataset_name, dataset_path)
        elif dataset_reader_type == ImplementedDatasetReaders.QAChave:
            dataset_reader = DatasetReaderQAChave(dataset_name, dataset_path)
        elif dataset_reader_type == ImplementedDatasetReaders.Antique:
            dataset_reader = DatasetReaderAntique(dataset_name, dataset_path)
        elif dataset_reader_type == ImplementedDatasetReaders.UIUC:
            dataset_reader = DatasetReaderUIUC(dataset_name, dataset_path)
        elif dataset_reader_type == ImplementedDatasetReaders.SQUAD:
            dataset_reader = DatasetReaderSQUAD(dataset_name, dataset_path)
        else:
            dataset_reader = None

        return dataset_reader
