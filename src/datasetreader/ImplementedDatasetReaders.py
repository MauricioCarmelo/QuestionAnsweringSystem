import enum


class ImplementedDatasetReaders(enum.Enum):
    DatasetUnknown = 1
    DatasetWikiPassageQA = 2    # reader_type = WikiPassageQA
    DatasetQAChave = 3          # reader_type = QAChave
