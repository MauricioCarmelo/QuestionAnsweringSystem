from src.datasetreader.DatasetReader import DatasetReader, QUESTION_COLUMNS
import logging
import pandas as pd


class DatasetWikiPassageQAReader(DatasetReader):

    def __init__(self):
        super(DatasetWikiPassageQAReader, self).__init__(name="WikiPassageQA")

    def load_entries(self):

        try:
            # df = pd.DataFrame(columns=QUESTION_COLUMNS.keys())
            questions = []
            # Load train file
            raw_df = pd.read_csv("../datasets/WikiPassageQA/train.tsv", sep='\t')
            for index, row in raw_df.iterrows():
                row = {"id": row["QID"], "question": row["Question"],
                       "answers": [{"documents": [{"id": row["DocumentID"], "name": row["DocumentName"]}],
                                    "passages": [{"passage": row["RelevantPassages"]}]}],
                       "pre_evaluation_group": "train",
                       }
                # df.append(row, ignore_index=True)
                questions.append(row)

            # Load dev file
            raw_df = pd.read_csv("../datasets/WikiPassageQA/dev.tsv", sep='\t')
            for index, row in raw_df.iterrows():
                row = {"id": row["QID"], "question": row["Question"],
                       "answers": [{"documents": [{"id": row["DocumentID"], "name": row["DocumentName"]}],
                                    "passages": [{"passage": row["RelevantPassages"]}]}],
                       "pre_evaluation_group": "dev",
                       }
                # df.append(row, ignore_index=True)
                questions.append(row)

            # Load test file
            raw_df = pd.read_csv("../datasets/WikiPassageQA/test.tsv", sep='\t')
            for index, row in raw_df.iterrows():
                row = {"id": row["QID"], "question": row["Question"],
                       "answers": [{"documents": [{"id": row["DocumentID"], "name": row["DocumentName"]}],
                                    "passages": [{"passage": row["RelevantPassages"]}]}],
                       "pre_evaluation_group": "test",
                       }
                # df.append(row, ignore_index=True)
                questions.append(row)

            # df is the concatenation of train, dev and test files.
            # The column pre_evaluation_group can identify the file.
            return questions

        except Exception as e:
            logging.error(str(e))
            return None
