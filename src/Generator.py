

class Generator:
    def __init__(self):
        pass

    def get_train_dev_test_sets(self, resource_entries):
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

        return train, dev, test
