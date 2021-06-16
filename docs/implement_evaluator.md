## How to implement another evaluator

If you want to evaluate a field or compare a field in such a way that the system does not support, it will be necessary
to implement an evaluator. In order to do this, please refer to the following steps:

1. Give you evaluator a name (this name will be used in the configuration file).
2. Create a class that extends `Evaluator` and save it at `"./src/evaluation"`.
3. Implement the abstract methods: 
    1. `Evaluator.evaluate_resource_entries()` 
       