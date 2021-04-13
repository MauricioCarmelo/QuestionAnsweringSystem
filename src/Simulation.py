import logging


class Simulation:
    def __init__(self, simulation_settings):
        self.simulation_settings = simulation_settings

        self.report = []
        self.questions = None

    def run(self):
 #       try:  # ToDo: include the TRY and logs here

        # For each dataset in config file
        for dataset_key in self.simulation_settings["datasets"]:
            print(dataset_key)
            # Load dataset
            dataset_settings = self.simulation_settings["datasets"][dataset_key]
            dataset = load_dataset(dataset_key)
            self.questions = dataset.load_entries()
            generator = self.cycles_generator(dataset_settings)

            # For each cycle
            cycle = 0
            for train_questions, dev_questions, test_questions in generator:
                print(f"    Cycle {cycle}")
                for task_key in self.simulation_settings["pipeline"]:
                    task_settings = self.simulation_settings["pipeline"][task_key]

                    if "datasets_ignore" in task_settings and dataset_key in task_settings["datasets_ignore"]:
                        print(f"        Dataset {dataset_key} ignored by the task {task_key}.")
                        continue

                    task = load_task(task_key)

                    if "technique" not in task_settings or "name" not in task_settings["technique"]:
                        print(f"Warning: Task {task_key} ignored once the technique was not configured.")
                        continue
                    technique_settings = task_settings["technique"]

                    task.technique = load_technique(technique_settings["name"])
                    task.technique.settings = technique_settings

                    # Todo: provide other types of resources for the task.execute.
                    _report = task.execute(train_questions, dev_questions, test_questions)
                    self.report.append(_report)

                    # ToDo: save the _report in a file

                    cycle += 1
        # ToDo: save the final self.report in a file
        self.present_report()

 #       except Exception as e:
 #           logging.error(str(e))

    def cycles_generator(self, dataset_settings):
        """ Return the cycles generator based in the dataset_settings. """
        if "evaluation" in dataset_settings and "type" in dataset_settings["evaluation"]:
            evaluation_settings = dataset_settings["evaluation"]
            evaluation_type = dataset_settings["evaluation"]["type"]
            if evaluation_type == "fixed-split":
                return self.generator_fixed_split()
            elif evaluation_type == "cross-validation":
                if "folds-splitter" in evaluation_settings:
                    folds_splitter = evaluation_settings["folds-splitter"]
                    if folds_splitter == "ShuffleSplit":
                        return self.generator_shuffle_split(evaluation_settings)
                    else:
                        return self.generator_kfold(evaluation_settings)
            else:
                return self.generator_all_test()
        else:
            return self.generator_all_test()

    def generator_fixed_split(self):
        """ It is a generator with one cycle. """
        train = []
        dev = []
        test = []
        for question in self.questions:
            if question["pre_evaluation_group"] == "train":
                train.append(question)
            elif question["pre_evaluation_group"] == "dev":
                dev.append(question)
            else:
                test.append(question)
        yield train, dev, test

    def generator_shuffle_split(self, evaluation_settings):
            from sklearn.model_selection import ShuffleSplit
            import numpy as np
            folds = 10
            if "folds" in evaluation_settings:
                folds = evaluation_settings["folds"]
            test_size = 0.3
            if "test_size" in evaluation_settings:
                test_size = evaluation_settings["test_size"]
            random_state = 0
            if "random_state" in evaluation_settings:
                random_state = evaluation_settings["random_state"]
            cv = ShuffleSplit(n_splits=folds, test_size=test_size, random_state=random_state)
            for train_index, test_index in cv.split(self.questions):
                questions = np.array(self.questions)
                train = questions[train_index]
                dev = []
                test = questions[test_index]
                yield train, dev, test

    def generator_kfold(self, evaluation_settings):
        from sklearn.model_selection import KFold
        import numpy as np
        folds = 10
        if "folds" in evaluation_settings:
            folds = evaluation_settings["folds"]
        cv = KFold(n_splits=folds)
        for train_index, test_index in cv.split(self.questions):
            questions = np.array(self.questions)
            train = questions[train_index]
            dev = []
            test = questions[test_index]
            yield train, dev, test

    def generator_all_test(self):
        """ It is a generator with one cycles where all questions are in the test set. """
        yield [], [], self.questions

    def present_report(self):
        print(self.report)


def load_dataset(dataset_key):
    """ Load a dataset instance according to the dataset_key parameter.
        :return: DatasetReader."""

    # ToDo: put this function in a correct place
    # ToDo: maybe integrate the file datasetreader.ImplementedDatasetReaders

    if dataset_key == "WikiPassageQA":
        from src.datasetreader.DatasetReaderWikiPassageQA import DatasetWikiPassageQAReader
        return DatasetWikiPassageQAReader()

    elif dataset_key == "QAChave":
        from src.datasetreader.DatasetReaderQAChave import DatasetReaderQAChave
        return DatasetReaderQAChave()


def load_task(task_key):
    """ Load a task instance according to the task_key parameter.
            :return: Task."""
    if task_key == "AnswerTypeClassification":
        from src.tasks.AnswerTypeClassification import AnswerTypeClassification
        return AnswerTypeClassification()


def load_technique(technique_key):
    """ Load a technique instance according to the technique_key parameter.
                :return: Technique."""
    if technique_key == "answer-type-simple-rule-based":
        from src.techniques.AnswerTypeSimpleRuleBased import AnswerTypeSimpleRuleBased
        return AnswerTypeSimpleRuleBased()