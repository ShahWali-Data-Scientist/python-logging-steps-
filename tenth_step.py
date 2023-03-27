# import logging
# logging.basicConfig(filename="test9.log", level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s  %(message)s')
#
# #create a function
# def devide(a,b) :
#     logging.info("the number entered by user is %s and %s", a,b)  #basic log to generate
#     try:
#         logging.info("we are into function")
#         div = a/b
#         logging.info("we have completed a division operations")
#         return  div
#     except Exception as e :
#         logging.exception(e)
# print(devide(3,6))


# second step

# import logging
# logging.basicConfig(filename="test9.log", level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s  %(message)s')
#
# #create a function
# def devide(a,b) :
#     logging.info("the number entered by user is %s and %s", a,b)  #basic log to generate
#     try:
#         logging.info("we are into function")
#         div = a/b
#         logging.info("we have completed a division operations")
#         return  div
#     except Exception as e :
#         logging.exception(e)
# print(devide(3,0))    # just change the numbers


# third way

import logging
logging.basicConfig(filename="test9.log", level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s  %(message)s')

#create a function
def devide(a,b) :
    logging.info("the number entered by user is %s and %s", a,b)  #basic log to generate
    try:
        logging.info("we are into function")
        div = a/b
        logging.info("we have completed a division operations")
        logging.info("result of code is %s ", div)
        return  div
    except Exception as e :
        logging.exception(e)
print(devide(3,7))    # just change the numbers