import pandas as pd
import time
import logging
logging.basicConfig(level=logging.DEBUG, filename='./logs/general.log')
logger = logging.getLogger()

"""
Constants Declaration
"""
KEYPATH = 'keys.pem'

"""
API - Key Reading and Writing Functions
"""


def read_keys():
    """
    Reads the keys from the specified KEYPATH and returns a list of keys as strings
    """
    keylist = []
    try:
        with open(KEYPATH, 'r') as f:
            keylist = f.readlines()
    except FileNotFoundError:
        logger.critical("Did not find the keyfile")
    keylist = [x.rstrip('\n') for x in keylist]
    logger.debug("Created the keylist.")
    return keylist


def create_keylogs(keylist):
    """
    Initializes a logging attempt for the alpha_vantage
    """
    d = {}
    for i in keylist:
        d[i] = None
    return d

def select_one_key(keydb):
    


def interday(self, ticker):
    """
    Returns interday data
    """
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={SYMBOL}&interval={INTERVAL}&apikey={API_KEY}&datatype=csv'
    pass





