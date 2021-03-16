from src.Simulation import Simulation
import logging
import json

logging.basicConfig(level=logging.DEBUG, filename='./log/my_logs.log')

if __name__ == '__main__':
    # main program
    with open("./config/config.json") as json_data_file:
        simulation1_settings = json.load(json_data_file)

    simulation = Simulation(simulation1_settings['simulation1'])
    simulation.run()