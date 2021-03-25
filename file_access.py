# write to file
def write2file():
	f = open('data.txt', 'w')
	f.write('some data')
	f.close()

def readfromfile():
# read from file
f = open('data.txt')
f.read()
f.close()

#write2file()
#readfromfile()

import os
os.listdir()

# make dir
#os.mkdir('newdir')

# remove file
#os.remove('data.txt')