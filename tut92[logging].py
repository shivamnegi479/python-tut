import logging
logging.basicConfig(filename="log.log",filemode="a",format='%(levelname)s %(asctime)s  %(lineno)d - %(message)s',
                        level='DEBUG')
for i in range(0,15):
    if(i%2==0):
        logging.warning("Log Warnning Message\n")
    else:
        logging.error("Logging Error Message\n")
