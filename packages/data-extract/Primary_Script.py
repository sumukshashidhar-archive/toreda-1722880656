## this is a simple script to scrape data




# curl -A "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0" https://www.nseindia.com/api/allIndices?csv=true -o sample.txt

## main imports, modelling will be done in jupyter
import os
from datetime import date
import time
import schedule


def get_csv(command):
	os.system(command)



def filename():
	name = date.today() + 
	return name


cmd = 'curl -A "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0" https://www.nseindia.com/api/allIndices?csv=true -o ' + filename
