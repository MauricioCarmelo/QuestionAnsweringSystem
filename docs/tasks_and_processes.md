## Tasks and processes
---

<details>
<summary>Load information from dataset</summary>

### Description

This process is divided in three parts:

* Load the information from the dataset.
* Generate `Question` objects to encapsulate all **data** and **metadata** related to a question.
* Parse the question text with a specific technique in order to generate a `query`. This `query` is also stored within
the `Question` object.

The outcome of this process is a list of questions, which will than be used to feed different **pipelines**.

### Sequence diagram

  ![](./images/question_to_query_process.png)

</details>
