## this is a simple script to scrape data




# curl -A "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0" https://www.nseindia.com/api/allIndices?csv=true -o sample.txt

## main imports, modelling will be done in jupyter
import os
from datetime import date
import time
import schedule

path = os.path.realpath('..')[:-8] + 'data' + '/indices' #path of the dataset_folder

def get_csv(command):
	os.system(command)



def filename():
	name = path + str(date.today()) + '.csv'
	return name


## defining some constants
cmd = 'curl -A "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0" https://www.nseindia.com/api/allIndices?csv=true -o '

def get():
	com = cmd + filename()
	get_csv(com)

schedule.every.day().at("21:00").do(get_csv)


while True:
	schedule.run_pending()
	time.sleep(1000)