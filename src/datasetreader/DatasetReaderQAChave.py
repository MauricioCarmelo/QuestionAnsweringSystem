from src.datasetreader.DatasetReader import DatasetReader
import xml.etree.ElementTree as ET


class DatasetReaderQAChave(DatasetReader):
    def load_entries(self):
        try:
            tree = ET.parse(self.path + '/questions.xml')
            root = tree.getroot()

            read_entries = []

            for pergunta in root:
                # Create an empty entry
                entry = {}

                entry['question'] = pergunta.find('texto').text

                if "id_org" in pergunta.attrib:
                    entry["id"] = pergunta.attrib["id_org"]

                if "tipo" in pergunta.attrib:
                    entry["answer_type"] = pergunta.attrib["tipo"]

                answers = []
                for resposta in pergunta.findall("resposta"):
                    answer = {}
                    answer["answer"] = resposta.text
                    if "n" in resposta.attrib:
                        answer["id"] = resposta.attrib["n"]
                    if "docid" in resposta.attrib:
                        answer["documents"] = [{"id": resposta.attrib["docid"]}]
                    answers.append(answer)
                entry["answers"] = answers

                read_entries.append(entry)

            return read_entries

        except Exception as e:
            print(str(e))
            return None