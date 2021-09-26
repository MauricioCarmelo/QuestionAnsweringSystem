import enum


class ImplementedDatasetReaders(enum.Enum):
    DatasetUnknown = 1
    WikiPassageQA = 2    # reader_type = WikiPassageQA
    QAChave = 3          # reader_type = QAChave
