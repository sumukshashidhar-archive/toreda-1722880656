import pandas as pd
import time


## Constants
KEYPATH = 'keys.pem'


def testingtest():
    return True

keylist = []
def read_keys():
    global keylist
    with open(KEYPATH, 'r') as f:
        keylist = f.readlines()
    keylist = [x.rstrip('\n') for x in keylist]
    return keylist

def create_keylogs():


x = read_keys()
print(keylist)



