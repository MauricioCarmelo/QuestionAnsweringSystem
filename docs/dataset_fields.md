## Configuration fields of file `datasets.yaml`
 
> **dataset**
>> **Mandatory:** Yes
>> 
>> **Parent:** -
>>
>> **Description:** Used to configure a dataset that might be used in the simulation.
>> 
>> **Values:** Block with fields `name`, `reader_type`, `path`, `dataset_setup`.
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
---

>**type**
>> **Mandatory:** Yes 
>> 
>> **Parent:** dataset_setup
>>
>> **Description:**
>> 
>> **Values:** `fixed-split` or `cross-validation`
---

>**folds_splitter**
>> **Mandatory:** Yes, if `type` is `cross-validation`
>> 
>> **Parent:** dataset_setup
>>
>> **Description:**
>> 
>> **Values:** `shuffle-split`
---

>**folds**
>> **Mandatory:** Yes, if `type` is equal to `cross-validation`
>> 
>> **Parent:** dataset_setup
>>
>> **Description:**
>> 
>> **Values:** Integer
---

>**test_size**
>> **Mandatory:** Yes, if `type` is equal to `cross-validation`
>> 
>> **Parent:** dataset_setup
>>
>> **Description:**
>>
>> ** Values:** Float
---

>**random_state**
>> **Mandatory:** Yes, if `type` is equal to `cross-validation`
>> 
>> **Parent:** dataset_setup
>>
>> **Description:**
>> 
>> **Values:**
---