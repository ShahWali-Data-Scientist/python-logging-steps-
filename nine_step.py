import logging
logging.basicConfig(filename="test8.log", level=logging.INFO,format='%(levelname)s %(asctime)s %(name)s  %(message)s')

#create a function
def devide(a,b) :
    logging.info("the number entered by user is %s and %s", a,b)  #basic log to generate
    return a/b
print(devide(3,6))