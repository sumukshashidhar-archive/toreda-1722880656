import pandas as pd
import os


dictionary = {}

files = os.listdir("./../../data/historical")

def compiler(FILE_LIST, name):
	dfs = []
	for each in FILE_LIST:
		dfs.append(pd.read_csv(each))
	final_frame = pd.concat(dfs, ignore_index=True)
	expstring = './../../data/historical_compiled/' + name + '.csv'
	final_frame.to_csv(expstring)



## just loops through and makes the files
for file in files:
	print(file)
	name = file[:-13]
	if name in dictionary.keys():
		dictionary[name].append(file)
	else:
		dictionary[name] = [file]



for key in dictionary.keys():
	print(dictionary[key])
	compiler(dictionary[key], key)
