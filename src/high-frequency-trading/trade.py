"""
Main trading file
"""

import datastream
from sentiment import sentiment_analysis
from lstmpredict import get_prediction
import mysql_interfacer
import time

prev_rows = mysql_interfacer.return_request_table_rows()
while True:
    diff = mysql_interfacer.return_request_table_rows()
    if diff == None:
        time.sleep(60)
    else:
        for i in diff:
            ## read the row difference and return
            get_prediction()
            mysql_interfacer.served()