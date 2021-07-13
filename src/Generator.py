from src.Settings import Settings


class Generator:
    @staticmethod
    def cycles_generator(resource_entries, dataset_name):
        dataset_setup = Settings.get_setup_settings(dataset_name)
        try:
            if dataset_setup['type'] == "fixed-split":
                return Generator.generator_fixed_split(resource_entries)
            elif dataset_setup['type'] == "cross-validation":
                if dataset_setup['folds_splitter'] == "shuffle-split":
                    return Generator.generator_shuffle_split(resource_entries,
                                                             dataset_setup['folds'],
                                                             dataset_setup['test_size'],
                                                             dataset_setup['random_state'])
                else:
                    return Generator.generator_kfold(resource_entries, dataset_setup['folds'])
            else:
                return Generator.generator_all_tests(resource_entries)
        except:
            pass

    @staticmethod
    def generator_fixed_split(resource_entries):
        train = []
        dev = []
        test = []

        for entry in resource_entries:
            if entry.get_value("pre_evaluation_group") == "train":
                train.append(entry)
            elif entry.get_value("pre_evaluation_group") == "dev":
                dev.append(entry)
            else:
                test.append(entry)
        yield train, dev, test

    @staticmethod
    def generator_shuffle_split(resource_entries, folds, test_size, random_state):
        from sklearn.model_selection import ShuffleSplit
        import numpy as np
        cv = ShuffleSplit(n_splits=folds, test_size=test_size, random_state=random_state)
        for train_index, test_index in cv.split(resource_entries):
            questions = np.array(resource_entries)
            train = questions[train_index]
            dev = []
            test = questions[test_index]
            yield train, dev, test

    @staticmethod
    def generator_kfold(resource_entries, folds):
        from sklearn.model_selection import KFold
        import numpy as np
        cv = KFold(n_splits=folds)
        for train_index, test_index in cv.split(resource_entries):
            questions = np.array(resource_entries)
            train = questions[train_index]
            dev = []
            test = questions[test_index]
            yield train, dev, test

    @staticmethod
    def generator_all_tests(resource_entries):
        """ It is a generator with one cycles where all questions are in the test set. """
        yield [], [], resource_entries
