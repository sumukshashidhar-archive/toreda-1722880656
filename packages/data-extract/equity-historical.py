# https://www.nseindia.com/api/historical/cm/equity?symbol=TECHM&series=[%22EQ%22]&from=11-04-2010&to=11-04-2012&csv=true

## this is a simple script to scrape data




# curl -A "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0" https://www.nseindia.com/api/allIndices?csv=true -o sample.txt



#TODO: Have to add a useragent randomizer
## main imports, modelling will be done in jupyter
import os
from datetime import date
import time
# import schedule


## change this if you move this file elsewhere
path = os.path.realpath('..')[:-8] + 'data' + '/historical/' #path of the dataset_folder
git_commit_path =  os.path.realpath('..')[:-8]


# to retrieve data from the NSE Server
def get_csv(command):
	os.system(command)

## to push to github
def push(FILENAME):
	pushcmd = 'git add ' + str(git_commit_path) + ' && git commit -a -m "File Commit: ' + str(FILENAME) + '" && git push'
	os.system(pushcmd)

#
# def filename():
# 	name = path + str(date.today()) + '.csv'
# 	return name
#


def urlmake(STOCK_NAME, DATE_RANGE, OUTPUT_NAME):
	'''

	:param STOCK_NAME: STRING the name of the stock that you want to scrape data for
	:param DATE_RANGE: a tuple with the start year and the end year
	:return: string which is the command url
	'''
	cmd = 'curl -A "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0" "https://www.nseindia.com/api/historical/cm/equity?symbol='+STOCK_NAME+'&series=[%22EQ%22]&from=11-04-'+str(DATE_RANGE[0])+'&to=11-04-'+str(DATE_RANGE[1])+'&csv=true" -o ' + str(OUTPUT_NAME)
	return cmd

## defining some constants

def get_data_for_all(STOCK_NAME, limit):
	'''

	:param STOCK_NAME: the name of the stock that you want to scrape
	:return:
	'''
	t = str(date.today())
	t = int(t[:4])
	datels = []
	while t - 2 >= limit:
		r = (t - 2, t)
		datels.append(r)
		t = t - 2
	for DATE_RANGE in datels:
		OUTPUT_NAME = '"' + str(STOCK_NAME + str(DATE_RANGE[0]) + '_'+ str(DATE_RANGE[1]) + '.csv') + '"'
		cmd = urlmake(STOCK_NAME, DATE_RANGE, OUTPUT_NAME)
		# print("EXECUTION IS", cmd)
		get_csv(cmd)
		time.sleep(5)
		push(OUTPUT_NAME)





a = True
inp = []
while a:
	x = input("Enter a Stock Symbol or blank to exit: \n")
	if x == '':
		a = False
		break
	else:
		inp.append(x)



# inp = eval(input("Please enter the stock names you wish to scrape in a proper python list format"))
limit = int(input("Please enter the furthest date that you wish to scrape back to. (DEFAULT IS 2010)"))


for stock in inp:
	get_data_for_all(stock, limit)


#
#
# def get():
# 	n = filename()
# 	com = cmd + n
# 	get_csv(com)
# 	time.sleep(100)
# 	pushcmd = push_cmd_1 + n[:-14] + push_cmd_2
# 	push(pushcmd)
#
# schedule.every().day.at("21:00").do(get)


#for testing
# get()
#
# while True:
# 	schedule.run_pending()
# 	print("Waiting")
# 	time.sleep(10000)