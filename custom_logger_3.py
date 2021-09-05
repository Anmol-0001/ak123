import logging

logger=logging.getLogger("Console and File Custom Logger")

logger.setLevel(logging.DEBUG)

#logger.setLevel(10)

consoleHandler=logging.StreamHandler()
consoleHandler.setLevel(logging.ERROR)

fileHandler=logging.FileHandler(filename="custom_logging.log",mode="w")

formatter1=logging.Formatter(" %(asctime)s : %(levelname)s : %(message)s",datefmt="%d/%m/%Y %I:%M:%S %p")

formatter2=logging.Formatter(" %(asctime)s : %(levelname)s : %(message)s",datefmt="%d/%m/%Y %H:%M:%S ")

consoleHandler.setFormatter(formatter1)

fileHandler.setFormatter(formatter2)

logger.addHandler(consoleHandler)

logger.addHandler(fileHandler)

logger.critical("critical message")

logger.error("error message")

logger.debug("debug message")


