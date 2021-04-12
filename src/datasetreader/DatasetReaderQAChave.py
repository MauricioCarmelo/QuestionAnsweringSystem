from src.datasetreader.DatasetReader import DatasetReader
import logging
import xml.etree.ElementTree as ET
import pandas as pd


class DatasetReaderQAChave(DatasetReader):
    def load_entries(self):
        fields = [x for x in self.fields_to_read]
        dataframe = pd.DataFrame(columns=fields)

        try:
            tree = ET.parse(self.path)
            root = tree.getroot()

            for pergunta in root:
                # Create an empty entry
                entry = {x: '' for x in self.fields_to_read}

                # Read expected fields from dataset
                for field in fields:
                    if field == 'texto':
                        entry[field] = pergunta.find('texto').text
                    else:
                        entry[field] = pergunta.get(field)

                # Insert value in the dataframe
                dataframe = dataframe.append(entry, ignore_index=True, verify_integrity=False, sort=None)

            return dataframe

        except Exception as e:
            logging.error(str(e))
            return None
