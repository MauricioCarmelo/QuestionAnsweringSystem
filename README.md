## Question Answering System
---

### Installation

Download the repository
> `git clone https://github.com/MauricioCarmelo/QuestionAnsweringSystem.git`

Setup environment
> `cd QuestionAnsweringSystem;`  
> `source ./setup.sh`

Install **pip** requirements
> `pip install -r requirements.txt`


### Execution

After making sure that files `config/dasetasets.yaml` and `config/pipeline.yaml` are configured
correctly, you can execute a simulation by running

`python3 ./src/main.py`

The results can be found inside folder `results/`.

### Documentation

* [Configuration file parameters](./docs/pipeline_configuration_file.md) (incomplete)

* [Glossary](./docs/glossary.md)

### How to contribute

* [Implement another dataset reader](./docs/implement_dataset_reader.md)

* [Implement another task and/or technique](docs/implement_task_and_technique.md)

* [~~Implement another evaluator~~](docs/implement_evaluator.md)