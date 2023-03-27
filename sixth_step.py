import logging
logging.basicConfig(filename="test5.log",level=logging.DEBUG,format='%(asctime)s %(message)s')
logging.info("This is my log with timestamp")