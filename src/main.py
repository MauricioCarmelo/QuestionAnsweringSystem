from src.Simulation import Simulation
from src.tasks.TaskGenerateQuery import TaskGenerateQuery
from src.Pipeline import Pipeline
import logging
import json
from Resource import Resource
from src.datasetreader.ImplementedDatasetReaders import ImplementedDatasetReaders

logging.basicConfig(level=logging.DEBUG, filename='./log/my_logs.log')

if __name__ == '__main__':
    simulation = Simulation()
    simulation.run()

