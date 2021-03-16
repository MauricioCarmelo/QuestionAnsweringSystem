from questionprocessing.QuestionProcessingDaemon import QuestionProcessingDaemon
import logging


class Simulation:
    def __init__(self, simulation_settings):
        self.simulation_settings = simulation_settings
        self.question_processing_daemon = None
        self.should_execute_question_processing = False
        self.should_execute_information_retrieval = False

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

