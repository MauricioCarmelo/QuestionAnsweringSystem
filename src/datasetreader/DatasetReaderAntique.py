from src.datasetreader.DatasetReader import DatasetReader
import pandas as pd


class DatasetReaderAntique(DatasetReader):
    def load_entries(self):
        try:
            resource_entries = []

            # raw_collection = pd.read_csv(self.path + '/antique-collection.txt', sep='\t',
            #                              names=["answer_id", "answer_text"])

            # Load test entries
            raw_train_dataframe_questions = pd.read_csv(self.path + '/antique-train-queries.txt', sep='\t',
                                                        names=["question_id", "question_text"])
            raw_train_dataframe_answers = pd.read_csv(self.path + '/antique-train.qrel', sep=' ',
                                                      names=["question_id", "answer_class", "answer_id", 'judgement'])

            for index_df_questions, row_df_questions in raw_train_dataframe_questions.iterrows():
                resource_entry = self.new_resource_entry()

                resource_entry.set_pre_evaluation_group("train")
                resource_entry.set_id(row_df_questions['question_id'])
                resource_entry.set_question(row_df_questions['question_text'])

                # Get answers
                possible_answers_df = raw_train_dataframe_answers[raw_train_dataframe_answers['question_id'] == row_df_questions['question_id']]
                if not possible_answers_df.empty:
                    for index_df_possible_answers, row_df_possible_answers in possible_answers_df.iterrows():
                        answer_id = row_df_possible_answers['answer_id']
                        # answers_df = raw_collection[raw_collection['answer_id'] == answer_id]
                        # if not answers_df.empty:
                        #     answer_text = answers_df['answer_text'].item()
                        # else:
                        #     answer_text = ''
                        answer_text=''

                        resource_entry.add_answer(id=answer_id, answer=answer_text)

                resource_entries.append(resource_entry)

            # release memory
            del raw_train_dataframe_questions
            del raw_train_dataframe_answers

            # Load test entries
            raw_test_dataframe_questions = pd.read_csv(self.path + '/antique-test-queries.txt', sep='\t',
                                                        names=["question_id", "question_text"])
            raw_test_dataframe_answers = pd.read_csv(self.path + '/antique-test.qrel', sep=' ',
                                                      names=["question_id", "answer_class", "answer_id", 'judgement'])

            for index_df_questions, row_df_questions in raw_test_dataframe_questions.iterrows():
                resource_entry = self.new_resource_entry()

                resource_entry.set_pre_evaluation_group("test")
                resource_entry.set_id(row_df_questions['question_id'])
                resource_entry.set_question(row_df_questions['question_text'])

                # Get answers
                possible_answers_df = raw_test_dataframe_answers[raw_test_dataframe_answers['question_id'] == row_df_questions['question_id']]
                if not possible_answers_df.empty:
                    for index_df_possible_answers, row_df_possible_answers in possible_answers_df.iterrows():
                        answer_id = row_df_possible_answers['answer_id']
                        # answers_df = raw_collection[raw_collection['answer_id'] == answer_id]
                        # if not answers_df.empty:
                        #     answer_text = answers_df['answer_text'].item()
                        # else:
                        #     answer_text = ''
                        answer_text = ''

                        resource_entry.add_answer(id=answer_id, answer=answer_text)

                resource_entries.append(resource_entry)

            # release memory
            del raw_test_dataframe_questions
            del raw_test_dataframe_answers
            # del raw_collection

            return resource_entries

        except Exception as e:
            print(str(e))
            return None
