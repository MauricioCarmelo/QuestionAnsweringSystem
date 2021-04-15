from src.Simulation import Simulation
from src.tasks.TaskSimpleSplit import TaskSimpleSplit
from src.Pipeline import Pipeline
import logging
import json

from Resource import Resource
from src.datasetreader.ImplementedDatasetReaders import ImplementedDatasetReaders

logging.basicConfig(level=logging.DEBUG, filename='./log/my_logs.log')

if __name__ == '__main__':
    # with open("./config/config.json") as json_data_file:
    #     simulation1_settings = json.load(json_data_file)
    #
    # simulation = Simulation(simulation1_settings['simulation1'])
    # simulation.run()

    # Tests and debug
    resource0 = Resource('WikiPassageQADev', ImplementedDatasetReaders.DatasetWikiPassageQA)
    resource0.build_resource_entries()

    task0 = TaskSimpleSplit(0)

    pipeline = Pipeline()
    pipeline.add_resource(resource0)
    pipeline.add_task(task0)

    pipeline.run_tasks()
