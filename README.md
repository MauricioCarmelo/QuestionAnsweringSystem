## Question Answering System
---

### Installation

#### Download the repository

> `git clone https://github.com/MauricioCarmelo/QuestionAnsweringSystem.git`

#### Setup environment

* Ubuntu terminal

```shell
cd QuestionAnsweringSystem   
pip install -r requirements.txt
```

Make sure variable PYTHONPATH has the absolute path to folder `QuestionAnsweringSystem`. Once inside folder 
`QuestionAnsweringSystem`, run:

```shell
export PYTHONPATH="$PWD":$PYTHONPATH
```

* PyCharm

On Run/Debug Configuration:  

**Script path:** path to `<path_to_project>/QuestionAnsweringSystem/src/main.py`  
**Working directory:** path to `<path_to_project>/QuestionAnsweringSystem/`

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