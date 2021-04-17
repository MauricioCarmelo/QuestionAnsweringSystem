from src.datasetreader.DatasetReader import DatasetReader
import logging
import pandas as pd


class DatasetReaderWikiPassageQA(DatasetReader):
    def load_entries(self):
        try:
            read_entries = []

            # Load train file
            raw_dataframe = pd.read_csv(self.path + '/train.tsv', sep='\t')
            for index, row in raw_dataframe.iterrows():
                row = {
                    "id": row["QID"],
                    "question": row["Question"],
                    "answers": [
                        {
                            "documents": [
                                {
                                    "id": row["DocumentID"],
                                    "name": row["DocumentName"],
                                }
                            ],
                            "passages": [
                                {
                                    "passage": row["RelevantPassages"]
                                }
                            ],
                        }
                    ],
                    "pre_evaluation_group": "train",
                }
                read_entries.append(row)

            # Load dev file
            raw_dataframe = pd.read_csv(self.path + '/dev.tsv', sep='\t')
            for index, row in raw_dataframe.iterrows():
                row = {
                    "id": row["QID"],
                    "question": row["Question"],
                    "answers": [
                        {
                            "documents": [
                                {
                                    "id": row["DocumentID"],
                                    "name": row["DocumentName"],
                                }
                            ],
                            "passages": [
                                {
                                    "passage": row["RelevantPassages"]
                                }
                            ],
                        }
                    ],
                    "pre_evaluation_group": "dev",
                }
                read_entries.append(row)

            # Load test file
            raw_dataframe = pd.read_csv(self.path + '/test.tsv', sep='\t')
            for index, row in raw_dataframe.iterrows():
                row = {
                    "id": row["QID"],
                    "question": row["Question"],
                    "answers": [
                        {
                            "documents": [
                                {
                                    "id": row["DocumentID"],
                                    "name": row["DocumentName"],
                                }
                            ],
                            "passages": [
                                {
                                    "passage": row["RelevantPassages"]
                                }
                            ],
                        }
                    ],
                    "pre_evaluation_group": "test",
                }
                read_entries.append(row)

            return read_entries

        except Exception as e:
            logging.error(str(e))
            return None
