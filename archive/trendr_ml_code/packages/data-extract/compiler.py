import pandas as pd
import os


dictionary = {}
git_commit_path =  os.path.realpath('..')[:-8]

files = os.listdir("./../../data/historical")
files.sort()


def push(FILENAME):
	pushcmd = 'git add ' + str(git_commit_path) + ' && git commit -a -m "File Commit: ' + str(FILENAME) + '" && git push'
	os.system(pushcmd)


def compiler(FILE_LIST, name):
	dfs = []
	for each in FILE_LIST:
		dfs.append(pd.read_csv("./../../data/historical/" + each))
	final_frame = pd.concat(dfs, ignore_index=True)
	expstring = './../../data/historical_compiled/' + name + '.csv'
	final_frame.to_csv(expstring)
	push(name)



## just loops through and makes the files
print(files)
for file in files:
	# print(file)
	name = file[:-13]
	if name in dictionary.keys():
		dictionary[name].append(file)
	else:
		dictionary[name] = [file]



for key in dictionary.keys():
	print(dictionary[key], key)
	compiler(dictionary[key], key)
