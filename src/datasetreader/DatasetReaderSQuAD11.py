from src.datasetreader.DatasetReader import DatasetReader
import logging
import json


class DatasetReaderSQuAD11(DatasetReader):

    def load_entries(self):

        try:
            f = open(self.path + 'dev-v1.1.json')
            data = json.load(f)

            """
                        json structure:

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

            # contexts = {}  # ToDo: in the future, load the contexts as a dataset resource (issue *)

            read_entries = []
            for d in data["data"]:
                for paragraph in d["paragraphs"]:
                    context = paragraph["context"]
                    # context_id = len(contexts)  # (issue *)
                    # contexts[context_id] = context  # (issue *)
                    for question in paragraph["qas"]:
                        entry = {}
                        entry["question"] = question["question"]
                        # entry["is_impossible"] = question["is_impossible"]
                        _answers = []
                        for answer in question["answers"]:
                            _answer = {"answer": answer["text"],
                                       "contexts": {"context": context,  # ToDo: use context ID (issue *)
                                                    "start_index_answer": answer["answer_start"]},
                                      }
                            _answers.append(_answer)
                        if "plausible_answers" in question:
                            for answer in question["plausible_answers"]:
                                _answer = {"answer": answer["text"],
                                           "contexts": {"context": context,  # ToDo: use context ID (issue *)
                                                        "start_index_answer": answer["answer_start"]},
                                          }
                                _answers.append(_answer)
                        entry["answers"] = _answers
                        read_entries.append(entry)
            return read_entries

        except Exception as e:
            logging.error(str(e))
            return None
