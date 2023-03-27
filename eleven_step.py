# import logging
#
# logging.basicConfig(filename= "test10.log",level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s  %(message)s')

# try :
#     logging.info("i am trynig to read a file")
#     with open("shah.txt", "r"):    # this name is dosen't exist
#         logging.info("succsfully it has read the file")
# except Exception as e :
#     logging.critical("this is a situation for us")
#     logging.error(e)
#
#
# # second way
# import logging
#
# logging.basicConfig(filename= "test10.log",level=logging.CRITICAL, format='%(levelname)s %(asctime)s %(name)s  %(message)s')
#
# try :
#     logging.info("i am trynig to read a file")
#     with open("shah.txt", "r"):    # this name is dosen't exist
#         logging.info("succsfully it has read the file")
# except Exception as e :
#     logging.critical("this is a situation for us")
#     logging.error(e)

# third way
import logging

logging.basicConfig(filename= "test10.log",level=logging.CRITICAL, format='%(levelname)s %(asctime)s %(name)s  %(message)s')

try :
    logging.info("i am trynig to read a file")
    with open("shah.txt", "r"):    # this name is dosen't exist
        logging.info("succsfully it has read the file")
except Exception as e :
    logging.critical("this is a situation for us")
    logging.error(e)
    logging.exception(e)
