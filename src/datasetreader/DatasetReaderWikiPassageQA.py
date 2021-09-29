from src.datasetreader.DatasetReader import DatasetReader
import pandas as pd


class DatasetReaderWikiPassageQA(DatasetReader):
    def load_entries(self):
        try:
            resource_entries = []

            # Load train file
            raw_dataframe = pd.read_csv(self.path + '/train.tsv', sep='\t')
            for index, row in raw_dataframe.iterrows():
                resource_entry = self.new_resource_entry()

                resource_entry.set_id(row["QID"])
                resource_entry.set_question(row["Question"])
                resource_entry.set_pre_evaluation_group("train")

                resource_entry.add_answer() # Create an answer with ID 0 to store documents and passages

                document_id = row['DocumentID']
                document_name = row['DocumentName']
                resource_entry.add_answer_document(doc_id=document_id, doc_name=document_name)

                relevant_passages = row["RelevantPassages"]
                relevant_passages = relevant_passages.split(',')

                passage_id = 0
                for passage in relevant_passages:
                    resource_entry.add_answer_passages(passage_id=passage_id, passage=passage)
                    # Decided to manually create an id to each passage
                    passage_id += 1

                resource_entries.append(resource_entry)

            # Load dev file
            raw_dataframe = pd.read_csv(self.path + '/dev.tsv', sep='\t')
            for index, row in raw_dataframe.iterrows():
                resource_entry = self.new_resource_entry()

                resource_entry.set_id(row["QID"])
                resource_entry.set_question(row["Question"])
                resource_entry.set_pre_evaluation_group("dev")

                resource_entry.add_answer()  # Create an answer with ID 0 to store documents and passages

                document_id = row['DocumentID']
                document_name = row['DocumentName']
                resource_entry.add_answer_document(doc_id=document_id, doc_name=document_name)

                relevant_passages = row["RelevantPassages"]
                relevant_passages = relevant_passages.split(',')

                passage_id = 0
                for passage in relevant_passages:
                    resource_entry.add_answer_passages(passage_id=passage_id, passage=passage)
                    # Decided to manually create an id to each passage
                    passage_id += 1

                resource_entries.append(resource_entry)

            # Load test file
            raw_dataframe = pd.read_csv(self.path + '/test.tsv', sep='\t')
            for index, row in raw_dataframe.iterrows():
                resource_entry = self.new_resource_entry()

                resource_entry.set_id(row["QID"])
                resource_entry.set_question(row["Question"])
                resource_entry.set_pre_evaluation_group("test")

                resource_entry.add_answer()  # Create an answer with ID 0 to store documents and passages

                document_id = row['DocumentID']
                document_name = row['DocumentName']
                resource_entry.add_answer_document(doc_id=document_id, doc_name=document_name)

                relevant_passages = row["RelevantPassages"]
                relevant_passages = relevant_passages.split(',')

                passage_id = 0
                for passage in relevant_passages:
                    resource_entry.add_answer_passages(passage_id=passage_id, passage=passage)
                    # Decided to manually create an id to each passage
                    passage_id += 1

                resource_entries.append(resource_entry)

            return resource_entries

        except Exception as e:
            print(str(e))
            return None
