## How to implement a dataset reader

If you want to read information from a dataset that is not supported by the application,it will be necessary to 
implement another **Dataset Reader**.

1. Give your dataset a name (this name will be used in the configuration file).

2. Create a new enumeration type in `ImplementedDatasetReaders`. This enumeration will be linked
   to a name that allude to the dataset itself. We suggest that you insert a comment in the 
   `ImplementedDatasetReaders` file with the name created on step 1, in front of the created type.
   
3. Create a class that extends `DatasetReader` and save it at `"./src/datasetreader/"`. 
   
4. Implement method `DatasetReader.load_entries()`. This method needs to return a `list()` of *Python* dictionaries,
where each dictionary represents a group of information in the dataset. The dictionary has the following
format:
   
   ```python
    record = {
       "id": None,
       "question": None,
       "question_domain": None,
       "answer_type": None,
       "answers": [{"id": None, "answer": None,
                    "documents": [{"id": None, "name": None, "document": None}],
                    "passages": [{"id": None, "name": None, "passage": None}],
                    "sentences": [{"id": None, "name": None, "sentence": None}]}
                   ],
       "entities": [{"entity": None, "start": None, "end": None, "type": None, "subtype": None}],
       "tokens": [],
   
       # When the collection contains a predefined division of training, dev, and test data,
       # this column determines which group this question belongs to. Possible values: None, 'train', 'dev', 'test'.
       "pre_evaluation_group": None,
       "evaluation_group": None
    }
    ```
   
   If the dataset does not have an information in particular, it is possible to leave that value empty; it
   is also possible to not insert the key, value pair.

5. Adjust method `BuilderDatasetReader.build_dataset_reader()` to return the correct class according to the 
recently created `ImplementedDatasetReaders` enum type.