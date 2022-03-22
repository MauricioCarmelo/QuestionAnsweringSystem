from src.evaluation.Evaluator import Evaluator
import numpy as np
import pandas as pd


class EvaluatorDocumentRanking(Evaluator):

    def evaluate(self, resource_entries):
        evaluation_results = {}
        results = []

        for resource_entry in resource_entries:
            question_text = resource_entry.get_value('question')
            answers = resource_entry.get_value('answers')
            answer_text = answers[0]['answer']

            for correct_value_field_name, predicted_value_field_name in self.field_mapping.items():

                document_ranking = resource_entry.get_value(predicted_value_field_name)
                binary_results = []
                for doc_name_and_score in document_ranking:
                    document_text = self.resource.get_articles()[doc_name_and_score[0]]
                    binary_results.append(int(answer_text.lower() in document_text.lower()))
                ans_in_res = int(any(binary_results))
                ap = self.average_precision(binary_results)

                rec = (ans_in_res, ap)
                results.append(rec)

        # format dataframe of results
        cols = ['is_answer_present', 'average_precision']
        results_df = pd.DataFrame(results, columns=cols)

        evaluation_results['recall'] = results_df.is_answer_present.value_counts(normalize=True)[1]
        evaluation_results['mean_average_precision'] =  results_df.average_precision.mean()

        return evaluation_results

    def average_precision(self, binary_results):
        m = 0
        precs = []
        for i, val in enumerate(binary_results):
            if val == 1:
                m += 1
                precs.append(sum(binary_results[:i + 1]) / (i + 1))
        ap = (1 / m) * np.sum(precs) if m else 0
        return ap
