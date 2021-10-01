## Configuration fields of file `datasets.yaml`
 
> **dataset**
>> **Mandatory:** Yes
>> 
>> **Parent:** -
>>
>> **Description:** Used to configure a dataset that might be used in the simulation.
>> 
>> **Values:** Block with fields `name`, `reader_type`, `path`, `dataset_setup`, `filter`.

**Example of block *'dataset'* with its children. Note that the children are incomplete in this example** 
```yaml
dataset:
  name: "QAChave"
  reader_type: "QAChave"
  path: "datasets/qa-chave/"
  dataset_setup:
    [block]
  filter:
    [block]
```
---

>**name**
>> **Mandatory:** Yes
>> 
>> **Parent:** dataset
>>
>> **Description:** Name of the dataset.
>>
>> **Values:** Any string. 
---

>**reader_type**
>> **Mandatory:** Yes
>> 
>> **Parent:** dataset
>>
>> **Description:** Type defined during the reader type implementation. This value is used to determine the
>> reader type class that will be instantiated on `NewSettings.determine_reader_type()`. This class is used to read the 
>> information of the dataset. 
>> 
>> **Values:** String
---

>**path**
>> **Mandatory:** Yes
>> 
>> **Parent:** dataset
>>
>> **Description:** Path to the dataset. Dataset samples are stored on folder `QuestionAnsweringSystem/datasets/`.
>> 
>> **Values:** String
---

>**dataset_setup**
>> **Mandatory:** Yes
>> 
>> **Parent:** datasets
>>
>> **Description:** Block used to configure the fold strategy that will be used during the load of a dataset resource.
>> 
>> **Values:** Block with fields `type`, `folds_splitter`, `folds`, `test_size`, `random_state`.
```yaml
  dataset_setup:
    type: "cross-validation"
    folds_splitter: "shuffle-split"
    folds: 5
    test_size: 0.4
    random_state: 0
```

>**type**
>> **Mandatory:** Yes 
>> 
>> **Parent:** dataset_setup
>>
>> **Description:**
>> 
>> **Values:** `fixed-split` or `cross-validation`
>
>**folds_splitter**
>> **Mandatory:** Yes, if `type` is `cross-validation`
>> 
>> **Parent:** dataset_setup
>>
>> **Description:**
>> 
>> **Values:** `shuffle-split`
>
>**folds**
>> **Mandatory:** Yes, if `type` is equal to `cross-validation`
>> 
>> **Parent:** dataset_setup
>>
>> **Description:**
>> 
>> **Values:** Integer
>
>**test_size**
>> **Mandatory:** Yes, if `type` is equal to `cross-validation`
>> 
>> **Parent:** dataset_setup
>>
>> **Description:**
>>
>> ** Values:** Float
>
>**random_state**
>> **Mandatory:** Yes, if `type` is equal to `cross-validation`
>> 
>> **Parent:** dataset_setup
>>
>> **Description:**
>> 
>> **Values:**
---
>**filter**
>> **Mandatory:** No
>> 
>> **Parent:** dataset
>>
>> **Description:** Mapping used to filter values from the resource entry. It receives a mapping where the key
>> is the name of the field in the resource entry and the value is a string. If there is a match between this string
>> and the content in the resource entry, the entry is filtered out.
>> 
>> **Values:** Mapping of fields.

**Example of block *'filter'***
```yaml
filter:
  answer_type: 'X'
```