import logging


class Simulation:
    def __init__(self, simulation_settings):
        self.simulation_settings = simulation_settings

        self.report = []
        self.questions = None

    def run(self):
        try:

            # For each dataset in config file
            for dataset_key in self.simulation_settings["datasets"]:
                print(dataset_key)
                # Load dataset
                dataset_settings = self.simulation_settings["datasets"][dataset_key]
                dataset = load_dataset(dataset_key)
                self.questions = dataset.load_entries()
                self.define_cycles(dataset_settings)

        except Exception as e:
            logging.error(str(e))

    def define_cycles(self, dataset_settings):
        """ Define how to perform the cycles. """
        if "evaluation" in dataset_settings and "type" in dataset_settings["evaluation"]:
            evaluation_type = dataset_settings["evaluation"]["type"]
            if evaluation_type == "fixed-split":
                self.define_fixed_split()
            elif evaluation_type == "cross-validation":
                self.define_folds(dataset_settings["evaluation"])
        else:
            self.define_all_test()

    def define_fixed_split(self):
        for question in self.questions:
            question["evaluation_group"] = "test"
            if "pre_evaluation_group" in question:
                question["evaluation_group"] = question["pre_evaluation_group"]

    def define_folds(self, evaluation_settings):
        if "folds-splitter" in evaluation_settings:
            if evaluation_settings["folds-splitter"] == "ShuffleSplit":
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
                fold = 0
                for train_index, test_index in cv.split(self.questions):
                    ...
                    # ToDo: think how perform the cross validations. Set the fold number is not a good idea.
                    #  I think it is better to iterate straight the self.questions with the fold-splitter model.

    def define_all_test(self):
        for question in self.questions:
            question["evaluation_group"] = "test"

    def define_cross_validation_group(self, evaluation_settings):
        ...


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
