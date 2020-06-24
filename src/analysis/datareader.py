import pandas as pd
import time
from datetime import date



## Constants
KEYPATH = 'keys.pem'


def testingtest():
    return True

keylist = []
def read_keys():
    global keylist
    with open(KEYPATH, 'r') as f:
        keylist = f.readlines()

print(keylist)



