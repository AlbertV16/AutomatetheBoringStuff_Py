import logging
logging.basicConfig(filename = 'myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# removes critical or lower messages
# logging.disable(logging.CRITICAL)

# logging.debug prints strings, using %s allows for variables to be printed easily in debug messages
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.info('i is %s, total is %s' % (i,total))

    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('End of program')

# Log levels (highest -> lowest)
# critical, error, warning, info, debug
