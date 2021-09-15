from src.Simulation import Simulation
import logging

logging.basicConfig(level=logging.DEBUG, filename='./log/my_logs.log')

if __name__ == '__main__':
    simulation = Simulation()
    simulation.run()
