from questionprocessing.QuestionProcessingDaemon import QuestionProcessingDaemon
import logging


class Simulation:
    question_processing_daemon = None
    simulation_settings = None

    should_execute_question_processing = False
    should_execute_information_retrieval = False

    def __init__(self, simulation_settings):
        self.simulation_settings = simulation_settings

        # check in the configuration file which steps should be executed
        if ("questionProcessing" in self.simulation_settings) and (self.simulation_settings["questionProcessing"]["should_execute"]):
            self.should_execute_question_processing = True
        if ("informationRetrieval" in self.simulation_settings) and (self.simulation_settings["informationRetrieval"]["should_execute"]):
            self.should_execute_information_retrieval = True

        if self.should_execute_question_processing:
            self.question_processing_daemon = QuestionProcessingDaemon(self.simulation_settings['questionProcessing'])

    def run(self):
        try:
            if self.should_execute_question_processing:
                logging.info("Running question processing daemon")
                self.question_processing_daemon.execute()
        except Exception as e:
            logging.error(str(e))

