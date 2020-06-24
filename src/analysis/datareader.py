import pandas as pd
import time
import logging
logging.basicConfig(level=logging.DEBUG, filename='./logs/general.log')
logger = logging.getLogger()

## Constants
KEYPATH = 'keys.pem'

def read_keys():
    keylist
    try:
        with open(KEYPATH, 'r') as f:
            keylist = f.readlines()
    except FileNotFoundError:
        logger.CRITICAL()
    keylist = [x.rstrip('\n') for x in keylist]
    logger.DEBUG()
    return keylist

def create_keylogs(keylist):
    d = {}
    for i in keylist:
        d[i] = None
    return d



def interday(self, ticker):
    url = f''
    pass



