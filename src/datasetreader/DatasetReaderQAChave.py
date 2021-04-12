from src.datasetreader.DatasetReader import DatasetReader
import logging
import xml.etree.ElementTree as ET
import pandas as pd


class DatasetReaderQAChave(DatasetReader):

    def __init__(self):
        super(DatasetReaderQAChave, self).__init__(name="QAChave")

    def load_entries(self):

        try:
            tree = ET.parse("dataset/qa-chave/questions.xml")
            root = tree.getroot()

            questions = []

            for pergunta in root:
                # Create an empty entry
                # Read expected fields from dataset
                question = {}
                question["question"] = pergunta.find('texto').text

                if "id_org" in pergunta.attrib:
                    question["id"] = pergunta.attrib["id_org"]

                if "tipo" in pergunta.attrib:
                    question["answer_type"] = pergunta.attrib["tipo"]

                answers = []
                for resposta in pergunta.findall("resposta"):
                    answer = {}
                    answer["answer"] = resposta.find('texto').text
                    if "n" in resposta.attrib:
                        answer["id"] = resposta.attrib["n"]
                    if "docid" in resposta.attrib:
                        answer["documents"] = [{"id": resposta.attrib["docid"]}]
                    answers.append(answer)
                question["answers"] = answers

                # In this case, question["pre_evaluation_group"] is empty once this dataset does not pre-split the data.

                questions.append(question)

            return questions

        except Exception as e:
            logging.error(str(e))
            return None
