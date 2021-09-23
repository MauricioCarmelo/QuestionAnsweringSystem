## Configuration fields of file `pipeline.yaml`

>**task**
>> **Mandatory:** Yes
>> 
>> **Parent:** -
>>
>> **Description:** 
>> 
>> **Values:** Block with fields `id`, `name`, `technique`, `predicts`, `used_datasets`, `evaluation`, `generated_result`.

**Example of block *'task'* with its childs. Note that the childs are incomplete in this example** 
```yaml
task:
  id: 1
  name: "answer_type_classification"
  technique: "RuleBased"
  predicts:
    [block]
  used_datasets:
    [block]
  evaluation:
    [block]
  generated_result: "result_task_1"
```
---

>**id**
>> **Mandatory:** Yes
>> 
>> **Parent:** task
>>
>> **Description:** Number that identifies the task in the pipeline.
>> 
>> **Values:** Integer
---

>**name**
>> **Mandatory:** Yes
>> 
>> **Parent:** task
>>
>> **Description:** Name of the task. This is the same name given by the person that implemented the task. It is very
>> important as it is used to instantiate the correct task class.
>> 
>> **Values:** String
---

>**technique**
>> **Mandatory:** Yes
>> 
>> **Parent:** task
>>
>> **Description:** Name of the technique. This is the same name given by the person that implemented the technique. It 
>> is very important as it is used to instantiate the correct technique class.
>> 
>> **Values:** String
---

>**predicts**
>> **Mandatory:** Yes
>> 
>> **Parent:** task
>>
>> **Description:** Specifies which set of entries (train, dev, test) should be used in the simulation.
>> 
>> **Values:** Block with fields `predict_train`, `predict_dev`, `predict_test`.
---

>**predict_train**
>> **Mandatory:** Yes
>> 
>> **Parent:** predicts
>>
>> **Description:** Used to set the usage of train entries in the simulation.
>> 
>> **Values:** Boolean
---

>**predict_dev**
>> **Mandatory:** Yes
>> 
>> **Parent:** predicts
>>
>> **Description:** Used to set the usage of dev entries in the simulation.
>> 
>> **Values:** Boolean
---

>**predict_test**
>> **Mandatory:** Yes
>> 
>> **Parent:** predicts
>>
>> **Description:** Used to set the usage of test entries in the simulation.
>> 
>> **Values:** Boolean

**Example of block *'predicts'***
```yaml
predicts:
  predict_train: false
  predict_dev: false
  predict_test: true 
```
---

>**used_datasets**
>> **Mandatory:** Yes
>> 
>> **Parent:** task
>>
>> **Description:**
>> 
>> **Values:**
---

>**dataset**
>> **Mandatory:** 
>> 
>> **Parent:** used_datasets
>>
>> **Description:**
>> 
>> **Values:**
---

>**name**
>> **Mandatory:** 
>> 
>> **Parent:** dataset
>>
>> **Description:**
>> 
>> **Values:**
---

>**input_fields**
>> **Mandatory:** 
>> 
>> **Parent:** dataset
>>
>> **Description:**
>> 
>> **Values:**
---
