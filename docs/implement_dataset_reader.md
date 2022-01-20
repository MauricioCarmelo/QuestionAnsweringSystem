## How to implement a dataset reader

If you want to read information from a dataset that is not supported by the application,it will be necessary to 
implement another **Dataset Reader**.

1. Give your dataset a name (this name will be used in the configuration file).

2. Create a new enumeration type in `ImplementedDatasetReaders`. This enumeration will be linked
   to a name that allude to the dataset itself. We suggest that you insert a comment in the 
   `ImplementedDatasetReaders` file with the name created on step 1, in front of the created type.
   
3. Create a class that extends `DatasetReader` and save it at `"./src/datasetreader/"`. 
   
4. Implement method `DatasetReader.load_entries()`. This method needs to return a `list()` of *resource entries*,
where each *resource entry* represents a group of information in the dataset. The resource entry has a *Python* dictionary
that has the following format:
   
   ```python
    ResourceEntry._field_value_mapping = {
       "id": None,
       "question": None,
       "question_domain": None,
       "answer_type": None,
       "answers": [{"id": None, "answer": None,
                    "documents": [{"id": None, "name": None, "document": None}],
                    "passages": [{"id": None, "name": None, "passage": None}],
                    "sentences": [{"id": None, "name": None, "sentence": None}]
                    }],
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
   
6. Adjust method `Settings.determine_reader_type()` to return the reader type accordingly.
   
### What to do while implementing method `DatasetReader.load_entries()`

This method is responsible for reading all the information related to the dataset and stored it in different resource
entries. Each resource entry is an instance of class *ResourceEntry*, that can be found on
`QuestionAnsweringSystem/src/ResourceEntry.py`.

First, create an empty list where all the resource entries will be appended to.

Then, as you read the information from the dataset, use method `DatasetReader.new_resource_entry()` to instantiate
the resource entry object. Note this method is called many times (inside a loop), as it is necessary one resource entry 
for each *question* in the dataset.

There are three things to take into consideration:

   1. You can use any technique or library you want to read the information from the dataset.
   2. You will have access to method `DatasetReader.new_resource_entry()` because if you are doing correctly so far your 
      dataset reader class is a child of `DatasetReader`.
   3. The information you read from the dataset need to be mapped to the instantiated resource entry.

#### Populating the Resource Entry

In order to populate the resource entry, there is a set of method that can be used for this. Refer to the following
methods signature from class `ResourceEntry`:


```python
set_id(self, id)
```
Set `_field_value_mapping['id']` value.

---

```python
set_question(self, question)
```
Set `_field_value_mapping['question']` value.

---

```python
set_question_domain(self, question_domain)
```
Set `_field_value_mapping['question_domain']` value.

---

```python
set_answer_type(self, answer_type)
```
Set `_field_value_mapping['answer_type']` value.

---

```python
set_evaluation_group(self, evaluation_group)
```
Set `_field_value_mapping['evaluation_group']` value.

---

```python
set_pre_evaluation_group(self, pre_evaluation_group)
```
Set `_field_value_mapping['pre_evaluation_group']` value.

---

```python
def add_entity(self, entity, start, end, type, subtype)
```
Add an entity in the *entities* array:
```python
_field_value_mapping['entities'] = [{
   "entity": None,
   "start": None, 
   "end": None, 
   "type": None, 
   "subtype": None}   
}]
```
---

```python
def add_token(self, token)
```
Add a token in the *tokens* array:

```python
_field_value_mapping['tokens'] = []
```
---

```python
def add_answer(self, id=0, answer='')
```
Adds an answer in the *answers* array:
```python
_field_value_mapping['entities'] = [{
   "id": 0, 
   "answer": '',
   "documents": [],
   "passages": [],
   "sentences": []
}]
```

---

```python
def add_answer_document(self, answer_id=0, doc_id=0, doc_name='', document='')
```
Adds a document in the *documents* array of an answer.
```python
_field_value_mapping['documents'] = [{
   "id": None,
   "name": None,
   "document": None   
}]
```
Note that in order to use `ResourceEntry.add_answer_document()` it is necessary to run `ResourceEntry.add_answer` first.

---

```python
def add_answer_passages(self, answer_id=0,  passage_id=0, passage_name='', passage='')
```
Adds a passage in the *passages* array of an answer.
```python
_field_value_mapping['passages'] = [{
   "id": None,
   "name": None,
   "passage": None   
}]
```
Note that in order to use `ResourceEntry.add_answer_passage()` it is necessary to run `ResourceEntry.add_answer` first.

---

```python
def add_answer_sentences(self, answer_id=0,  sentence_id=0, sentence_name='', sentence='')
```
Adds a sentence in the *sentences* array of an answer.
```python
_field_value_mapping['sentences'] = [{
   "id": None,
   "name": None,
   "sentence": None   
}]
```
Note that in order to use `ResourceEntry.add_answer_senteces()` it is necessary to run `ResourceEntry.add_answer` first.

---