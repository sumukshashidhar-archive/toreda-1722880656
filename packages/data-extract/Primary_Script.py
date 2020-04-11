## this is a simple script to scrape data




# curl -A "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0" https://www.nseindia.com/api/allIndices?csv=true -o sample.txt

## main imports, modelling will be done in jupyter
import os
from datetime import date
import time
import schedule

path = os.path.realpath('..')[:-8] + 'data' + '/indices' #path of the dataset_folder
push_cmd_1 = 'git add' + path + ' && git commit -a -m "File Commit: '
push_cmd_2 = '" && git push'

def get_csv(command):
	os.system(command)


def push(pushcmd):
	os.system(pushcmd)


def filename():
	name = path + str(date.today()) + '.csv'
	return name


## defining some constants
cmd = 'curl -A "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0" https://www.nseindia.com/api/allIndices?csv=true -o '

def get():
	n = filename()
	com = cmd + n
	get_csv(com)
	time.sleep(100)
	pushcmd = push_cmd + n + push_cmd_2
	push(pushcmd)

schedule.every.day().at("21:00").do(get)


while True:
	schedule.run_pending()
	time.sleep(10000)