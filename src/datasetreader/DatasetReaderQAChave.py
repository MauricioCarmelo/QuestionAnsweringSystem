from src.datasetreader.DatasetReader import DatasetReader
import xml.etree.ElementTree as ET


class DatasetReaderQAChave(DatasetReader):
    def load_entries(self):
        try:
            tree = ET.parse(self.path + '/questions.xml')
            root = tree.getroot()

            resource_entries = []

            for pergunta in root:
                resource_entry = self.new_resource_entry()

                resource_entry.set_question(pergunta.find('texto').text)

                if "id_org" in pergunta.attrib:
                    resource_entry.set_id(pergunta.attrib["id_org"])

                if "tipo" in pergunta.attrib:
                    resource_entry.set_answer_type(pergunta.attrib["tipo"])

                for resposta in pergunta.findall("resposta"):
                    answer_text = resposta.text
                    if "n" in resposta.attrib:
                        answer_id = resposta.attrib["n"]
                    else:
                        answer_id = 0
                    resource_entry.add_answer(answer_id, answer_text)

                    if "docid" in resposta.attrib:
                        document_id = resposta.attrib["docid"]
                        resource_entry.add_answer_document(answer_id, document_id)

                resource_entries.append(resource_entry)

            return resource_entries

        except Exception as e:
            print(str(e))
            return None