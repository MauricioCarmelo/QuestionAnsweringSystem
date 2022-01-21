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
                resource_entry.set_answer_type(self.normalize_answer_type(row_df_questions['answer_type'],
                                                                          row_df_questions['domain']))
                resource_entry.set_question_domain(row_df_questions['domain'])

                resource_entries.append(resource_entry)

            # Load test entries
            raw_test_dataframe_questions = pd.read_csv(self.path + '/test.csv', sep=',',
                                                        names=["question_id", "answer_type", "question_text",
                                                               "domain"],
                                                        skiprows=1)

            for index_df_questions, row_df_questions in raw_test_dataframe_questions.iterrows():
                resource_entry = self.new_resource_entry()
                resource_entry.set_pre_evaluation_group("test")
                resource_entry.set_id(row_df_questions['question_id'])
                resource_entry.set_question(row_df_questions['question_text'])
                resource_entry.set_answer_type(self.normalize_answer_type(row_df_questions['answer_type'],
                                                                          row_df_questions['domain']))
                resource_entry.set_question_domain(row_df_questions['domain'])

                resource_entries.append(resource_entry)

            return resource_entries

        except Exception as e:
            print(str(e))
            return None

    def normalize_answer_type(self, question_type, domain):
        if question_type == 'NUM' and domain == 'date':
            return 'TIME'
        if question_type == 'NUM':
            return 'MEASURE'
        if question_type == 'ENTY':
            return 'OTHER'
        if question_type == 'LOC':
            return 'LOCATION'
        if question_type == 'HUM':
            return 'PERSON'
        if question_type == 'DESC':
            return 'OTHER'
        return 'OTHER'
