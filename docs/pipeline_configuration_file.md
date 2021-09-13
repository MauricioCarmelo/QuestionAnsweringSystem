# Understand the pipeline configuration file

### Documentation fields

All fields in the block are `required`, unless specified.

**datasets**
> **Mandatory:** 
> 
> **Father:** -
>
> **Description:** Used to configure the datasets that might be used in the simulation.
> 
> **Values:** Block with fields `reader_type`, `name`, `path`, `dataset_setup`
---

**reader_type**
> **Mandatory:** 
> 
> **Father:** datasets
>
> **Description:**
> 
> **Values:**
---

**name**
> **Mandatory:** 
> 
> **Father:** datasets
>
> **Description:**
>
> **Values:** 
---

**path**
> **Mandatory:** 
> 
> **Father:** datasets
>
> **Description:**
> 
> **Values:**
---

**dataset_setup**
> **Mandatory:** 
> 
> **Father:** datasets
>
> **Description:**
> 
> **Values:** > **Values:** Block with fields `type`, `folds_splitter`, `folds`, `test_size`
---

**type**
> **Mandatory:** 
> 
> **Father:** dataset_setup
>
> **Description:**
> 
> **Values:**
---

**folds_splitter**
> **Mandatory:** 
> 
> **Father:** dataset_setup
>
> **Description:**
> 
> **Values:**
---

**folds**
> **Mandatory:** 
> 
> **Father:** dataset_setup
>
> **Description:**
> 
> > **Values:**
---

**test_size**
> **Mandatory:** 
> 
> **Father:** dataset_setup
>
> **Description:**
---

**random_state**
> **Mandatory:** 
> 
> **Father:** dataset_setup
>
> **Description:**
> 
> **Values:**
---

**pipeline**
> **Mandatory:** 
> 
> **Father:** -
>
> **Description:**
> 
> **Values:**
---

**tasks**
> **Mandatory:** 
> 
> **Father:** pipeline
>
> **Description:**
> 
> **Values:**
---

**task**
> **Mandatory:** 
> 
> **Father:** tasks
>
> **Description:**
> 
> **Values:**
---

**id**
> **Mandatory:** 
> 
> **Father:** task
>
> **Description:**
> 
> **Values:**
---

**ignore**
> **Mandatory:** 
> 
> **Father:** task
>
> **Description:**
> 
> **Values:**
---

**name**
> **Mandatory:** 
> 
> **Father:** task
>
> **Description:**
> 
> **Values:**
---

**technique**
> **Mandatory:** 
> 
> **Father:** task
>
> **Description:**
> 
> **Values:**
---

**predicts**
> **Mandatory:** 
> 
> **Father:** task
>
> **Description:**
> 
> **Values:**
---

**predict_train**
> **Mandatory:** 
> 
> **Father:** predicts
>
> **Description:**
> 
> **Values:**
---

**predict_dev**
> **Mandatory:** 
> 
> **Father:** predicts
>
> **Description:**
> 
> **Values:**
---

**predict_test**
> **Mandatory:** 
> 
> **Father:** predicts
>
> **Description:**
> 
> **Values:**
---

**used_datasets**
> **Mandatory:** 
> 
> **Father:** task
>
> **Description:**
> 
> **Values:**
---

**used_dataset**
> **Mandatory:** 
> 
> **Father:** used_datasets
>
> **Description:**
> 
> **Values:**
---

**name**
> **Mandatory:** 
> 
> **Father:** used_dataset
>
> **Description:**
> 
> **Values:**
---

**input_fields**
> **Mandatory:** 
> 
> **Father:** used_dataset
>
> **Description:**
> 
> **Values:**
---

**evaluation**
> **Mandatory:** 
> 
> **Father:** task
>
> **Description:**
> 
> **Values:**
---

**type**
> **Mandatory:** 
> 
> **Father:** evaluation
>
> **Description:**
> 
> **Values:**
---

**should_evaluate**
> **Mandatory:** 
> 
> **Father:** evaluation
>
> **Description:**
> 
> **Values:**
---

**fields**
> **Mandatory:** 
> 
> **Father:** evaluation
>
> **Description:**
> 
> **Values:**
---

**metrics**
> **Mandatory:** 
> 
> **Father:** evaluation
>
> **Description:**
> 
> **Values:**
---

**fi_score**
> **Mandatory:** 
> 
> **Father:** metrics
>
> **Description:**
> 
> **Values:**
---