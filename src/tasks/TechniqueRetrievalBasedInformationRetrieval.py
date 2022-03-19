from src.tasks.Technique import Technique
from elasticsearch import Elasticsearch
import os
from subprocess import Popen, PIPE, STDOUT


class TechniqueRetrievalBasedInformationRetrieval(Technique):

    def run(self, resource_entries):
        results = []
        for resource_entry in resource_entries:
            result = self.__run_technique(resource_entry)
            results.append(result)
        return results

    def __run_technique(self, resource_entry):
        if self.es_object is None:
            self.es_object = Elasticsearch({'host': 'localhost', 'port': 9200, 'scheme': "http"})

        question_text = resource_entry.get_value('question')

        query = {
            'query': {
                'match': {
                    'document_text': question_text
                }
            }
        }

        res = self.es_object.search(index=self.index_name, body=query, size=10)
        # print(f'Question: {question_text}')
        # print(f'Query Duration: {res["took"]} milliseconds')
        # print('Title, Relevance Score:')
        return [(hit['_source']['document_title'], hit['_score']) for hit in res['hits']['hits']]

    def setup(self):
        self.index_name = 'squad-standard-index'
        self.index_config = {
            "settings": {
                "analysis": {
                    "analyzer": {
                        "standard_analyzer": {
                            "type": "standard"
                        }
                    }
                }
            },
            "mappings": {
                "dynamic": "strict",
                "properties": {
                    "document_title": {"type": "text", "analyzer": "standard_analyzer"},
                    "document_text": {"type": "text", "analyzer": "standard_analyzer"}
                }
            }
        }
        self.es_object = Elasticsearch({'host': 'localhost', 'port': 9200, 'scheme': "http"})

    def train(self, train_set, dev_set, test_set, resource_articles):
        if self.es_object.indices.exists(index=self.index_name):
            self.es_object.indices.delete(index=self.index_name)
        self.es_object.indices.create(index=self.index_name, body=self.index_config, ignore=400)

        i=0
        for article_title, article_text in resource_articles.items():
            index_status = self.es_object.index(index=self.index_name, id=i, body={'document_title': article_title,
                                                                                   'document_text': article_text})
            i = i+1

    def validate(self, dev_set):
            pass
