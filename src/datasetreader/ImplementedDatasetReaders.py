import enum


class ImplementedDatasetReaders(enum.Enum):
    DatasetUnknown = 1
    WikiPassageQA = 2    # reader_type = WikiPassageQA
    QAChave = 3          # reader_type = QAChave
    Antique = 4          # reader_type = Antique
    UIUC = 5             # reader_type = UIUC
