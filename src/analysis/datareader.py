import pandas as pd
import time
import logging
logging.basicConfig(level=logging.DEBUG, filename='./analysis/logs/general.log')
logger = logging.getLogger()

"""
Constants Declaration
"""
KEYPATH = './analysis/keys.pem'

"""
API - Key Reading and Writing Functions
"""


def read_keys():
    """
    Reads the keys from the specified KEYPATH and returns a dictionary of keys, along with unix timestamps of their use
    """
    keylist = []
    try:
        with open(KEYPATH, 'r') as f:
            keylist = f.readlines()
    except FileNotFoundError:
        logger.critical("Did not find the keyfile")
    keylist = [x.rstrip('\n') for x in keylist]
    logger.debug("Created the keylist.")
    d = {}
    for i in keylist:
        d[i] = 0
    return d


def select_one_key(keydb):
    """
    Returns the least recently used key in the current dictionary. This assists with high frequency data analysis.

    @params
    keydb = dictionary
    """
    cur_time = time.time()
    max_time = 0
    max_time_key = None
    for i in keydb.keys():
        if cur_time - keydb[i] > max_time:
            max_time_key = i
            max_time = cur_time - keydb[i]
    keydb[max_time_key] = cur_time
    return max_time_key, keydb


def interday(self, ticker, interval, key):
    """
    Returns interday data
    """
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={ticker}&interval={interval}&apikey={key}&datatype=csv'
    df = pd.read_csv(url)
    return df





