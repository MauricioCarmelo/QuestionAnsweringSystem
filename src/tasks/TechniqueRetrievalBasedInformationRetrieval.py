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
        pass

    def setup(self):
        self.es_object = Elasticsearch({'host': 'localhost', 'port': 9200, 'scheme': "http"})
        index_config = {
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

        self.index_name = 'squad-standard-index'
        if self.es_object.indices.exists(index=self.index_name):
            self.es_object.indices.delete(index=self.index_name)
        self.es_object.indices.create(index=self.index_name, body=index_config, ignore=400)

    def train(self, train_set, dev_set, test_set, resource_articles):
        # for i, resource_entry in enumerate(train_set + dev_set):
        i=0
        for article_title, article_text in resource_articles.items():
            index_status = self.es_object.index(index=self.index_name, id=i, body={'document_title': article_title,
                                                                                   'document_text': article_text})
            i = i+1


        n_records = self.es_object.count(index=self.index_name)['count']
        print(f'Succesfully loaded {n_records} into {self.index_name}')

    def validate(self, dev_set):
        pass
