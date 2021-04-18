from src.datasetreader.DatasetReader import DatasetReader
import logging
import json


class DatasetReaderSQuAD11(DatasetReader):

    def load_entries(self):

        try:
            read_entries = []

            # train-v1.1.json file
            f = open(self.path + 'train-v1.1.json')
            read_entries += self.__read_squad_json_format(f, "train")

            # dev-v1.1.json file
            f = open(self.path + 'dev-v1.1.json')
            read_entries += self.__read_squad_json_format(f, "dev")

            return read_entries

        except Exception as e:
            logging.error(str(e))
            return None

    def __read_squad_json_format(self, file, pre_evaluation_group):
        """
        It read a json file SQuAD format and return its resource entries.

        json SQuAD file structure:
            version
            data (list)
                title
                paragraphs (list)
                    qas (list)
                        question
                        id
                        is_impossible
                        context
                        answers (list)
                            text
                            answer_start
                        plausible_answers (list)
                            text
                            answer_start
        """
        data = json.load(file)

        # contexts = {}  # ToDo: in the future, load the contexts as a dataset resource (issue 27)

        read_entries = []
        for d in data["data"]:
            for paragraph in d["paragraphs"]:
                context = paragraph["context"]
                # context_id = len(contexts)  # (issue 27)
                # contexts[context_id] = context  # (issue 27)
                for question in paragraph["qas"]:
                    entry = {}
                    entry["question"] = question["question"]
                    if "is_impossible" in question:
                        entry["is_impossible"] = question["is_impossible"]
                    _answers = []
                    for answer in question["answers"]:
                        _answer = {"answer": answer["text"],
                                   "contexts": {"context": context,  # ToDo: use context ID (issue 27)
                                                "start_index_answer": answer["answer_start"]},
                                   }
                        _answers.append(_answer)
                    if "plausible_answers" in question:
                        for answer in question["plausible_answers"]:
                            _answer = {"answer": answer["text"],
                                       "contexts": {"context": context,  # ToDo: use context ID (issue 27)
                                                    "start_index_answer": answer["answer_start"]},
                                       }
                            _answers.append(_answer)
                    entry["answers"] = _answers
                    entry["pre_evaluation_group"] = pre_evaluation_group
                    read_entries.append(entry)
        return read_entries
