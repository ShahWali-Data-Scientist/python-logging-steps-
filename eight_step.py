import logging
# logging.basicConfig(filename="test7.log",level=logging.DEBUG,format='%(asctime)s %(name)s %(levelname)s %(message)s')
# logging.info("This is my log with timestamp")
#sequence
logging.basicConfig(filename="test7.log",level=logging.DEBUG,format='%(levelname)s %(asctime)s %(name)s  %(message)s')
logging.info("This is my log with timestamp")