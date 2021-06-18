import logging

class log_gen:
    """ This class will define implentation for logging patterns"""

    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\logs\\automation.logs",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y $I:%M:%S %p'
                            )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger