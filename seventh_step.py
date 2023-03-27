import logging
logging.basicConfig(filename="test6.log",level=logging.DEBUG,format='%(asctime)s %(name)s %(message)s')
logging.info("This is my log with timestamp")