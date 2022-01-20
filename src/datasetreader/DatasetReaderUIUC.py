from src.datasetreader.DatasetReader import DatasetReader
import pandas as pd


class DatasetReaderUIUC(DatasetReader):
    def load_entries(self):
        try:
            resource_entries = []

            # Load train entries
            raw_train_dataframe_questions = pd.read_csv(self.path + '/train.csv', sep=',',
                                                        names=["question_id", "answer_type", "question_text", "domain"],
                                                        skiprows=1)

            for index_df_questions, row_df_questions in raw_train_dataframe_questions.iterrows():
                resource_entry = self.new_resource_entry()
                resource_entry.set_pre_evaluation_group("train")
                resource_entry.set_id(row_df_questions['question_id'])
                resource_entry.set_question(row_df_questions['question_text'])
                resource_entry.set_answer_type(row_df_questions['answer_type'])
                resource_entry.set_question_domain(row_df_questions['domain'])

                resource_entries.append(resource_entry)

            return resource_entries

        except Exception as e:
            print(str(e))
            return None
