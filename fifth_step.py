import logging
logging.basicConfig(filename="test4.log",level= logging.INFO)
logging.info("This is my first code for logging")
logging.warning("This will try to load a warning message")
logging.error("This is a error message from sysytem")
l = [1,2,3,4,5,6,7,7]
for i in l :
    if i == 2 :
        logging.info(l)
        logging.warning("this is a warning for a user that they have found out 2 in list")
logging.shutdown()