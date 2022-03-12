from src.datasetreader.DatasetReader import DatasetReader
import json


class DatasetReaderSQUAD(DatasetReader):

    def load_entries(self):
        try:
            self.train_file = self.path + "/train-v2.0.json"
            self.dev_file = self.path + "/dev-v2.0.json"

            train_dataset= json.load(open(self.train_file, 'rb'))
            dev_dataset = json.load(open(self.dev_file, 'rb'))

            resource_entries = []
            wiki_articles = {}

            # load train
            for article in train_dataset['data']:
                for i, paragraph in enumerate(article['paragraphs']):
                    used_article = article['title'] + f'_{i}'
                    for questions in paragraph['qas']:
                        resource_entry = self.new_resource_entry()
                        resource_entry.set_id(questions['id'])
                        resource_entry.set_question(questions['question'])
                        resource_entry.set_pre_evaluation_group("train")
                        try:
                            resource_entry.add_answer(answer=questions['answers'][0]['text'])
                        except:
                            resource_entry.add_answer(answer="")
                        resource_entry.set_indexed_article(used_article)

                        resource_entries.append(resource_entry)

            # load dev
            for article in dev_dataset['data']:
                for i, paragraph in enumerate(article['paragraphs']):
                    used_article = article['title'] + f'_{i}'
                    for questions in paragraph['qas']:
                        resource_entry = self.new_resource_entry()
                        resource_entry.set_id(questions['id'])
                        resource_entry.set_question(questions['question'])
                        resource_entry.set_pre_evaluation_group("dev")
                        try:
                            resource_entry.add_answer(answer=questions['answers'][0]['text'])
                        except:
                            resource_entry.add_answer(answer="")
                        resource_entry.set_indexed_article(used_article)

                        resource_entries.append(resource_entry)
            return resource_entries

        except Exception as e:
            print(str(e))

    def load_articles(self):
        try:
            self.train_file = self.path + "/train-v2.0.json"
            self.dev_file = self.path + "/dev-v2.0.json"

            train_dataset = json.load(open(self.train_file, 'rb'))
            dev_dataset = json.load(open(self.dev_file, 'rb'))

            wiki_articles = {}

            # load train
            for article in train_dataset['data']:
                for i, paragraph in enumerate(article['paragraphs']):
                    wiki_articles[article['title'] + f'_{i}'] = article['title'] + ' ' + paragraph['context']

            # load dev
            for article in dev_dataset['data']:
                for i, paragraph in enumerate(article['paragraphs']):
                    wiki_articles[article['title'] + f'_{i}'] = article['title'] + ' ' + paragraph['context']

            return wiki_articles

        except Exception as e:
            print(str(e))
