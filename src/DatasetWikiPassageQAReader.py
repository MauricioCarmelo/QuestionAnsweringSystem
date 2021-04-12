from DatasetReader import DatasetReader
import logging
import pandas as pd


class DatasetWikiPassageQAReader(DatasetReader):
    def load_entries(self):
        fields = [x for x in self.fields_to_read]
        try:
            data = pd.read_csv(self.path, sep='\t', usecols=fields)
            return data

        except Exception as e:
            logging.error(str(e))
            return None
