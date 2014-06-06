#!/usr/bin/python
#encoding=utf-8

import sys, string
from coordmap import mapDict, down, ntlevel, up, clickNum

# mouse delay
mDelay = 300
# question delay
qDelay = 2000
# level delay
lDelay = 2000

def genscript(level, start, mapDict, mDelay, qDelay) :
	# customed coordinates file
	coordfile = './coordinates/coord_' + str(level) + '.txt'
	coordfile = open(coordfile, 'r')
	for i in range(start - 1) :
		discard = coordfile.readline()
	coords = coordfile.readlines()
	coordfile.close()
	script = ''
	for coordsline in coords :
		coordsline = coordsline[4:].strip('\r\n')
		coordslist = coordsline.split(', ')
		# one answer includes multiple coordinates
		for coord in coordslist :
			script = script + '坐标：' + mapDict[coord] + '\r\n'
			script = script + '鼠标：左键\r\n'
			script = script + '延时：' + str(mDelay) + '\r\n'
		script = script + '延时：' + str(qDelay) + '\r\n'
	return script

def genscriptall(level, start, mapDict, mDelay, qDelay, lDelay, up, ntlevel, down, clickNum) :
	assert type(level) == int
	assert type(start) == int
	assert type(mapDict) == dict
	assert type(qDelay) == int
	assert type(lDelay) == int
	assert type(up) == str
	assert type(ntlevel) == str
	assert type(down) == str
	assert type(clickNum) == int
	# script file
	scriptfile = './scripts/script.txt'
	scriptfile = open(scriptfile, 'w+')
	scriptfile.write('循环：1\r\n')
	for idx in range(level, 7, 1) :
		if (idx == level) :
			scriptfile.write(genscript(idx, start, mapDict, mDelay, qDelay))
		else :
			scriptfile.write(genscript(idx, 1, mapDict, mDelay, qDelay))
		# page down
		scriptfile.write('坐标: ' + down + '\r\n')
		for i in range(clickNum) :
			scriptfile.write('鼠标：左键\r\n')
			scriptfile.write('延时：' + str(mDelay) + '\r\n')
		scriptfile.write('延时：' + str(mDelay) + '\r\n')
		# next game level
		scriptfile.write('延时：' + str(lDelay) + '\r\n')
		scriptfile.write('坐标：' + ntlevel + '\r\n')
		scriptfile.write('鼠标：左键\r\n')
		scriptfile.write('延时：' + str(mDelay) + '\r\n')
		# page up
		scriptfile.write('坐标：' + up + '\r\n')
		for i in range(clickNum) :
			scriptfile.write('鼠标：左键\r\n')
			scriptfile.write('延时：' + str(mDelay) + '\r\n')
		scriptfile.write('延时：' + str(mDelay) + '\r\n')
	scriptfile.close()	

def chkArgv(level, start) :
	assert type(level) == str
	assert type(start) == str
	level = string.atoi(level)
	start = string.atoi(start)
	if (level == 1 and start >= 1 and start <= 20) :
		pass
	elif (level == 2 and start >= 1 and start <= 20) :
		pass
	elif (level == 3 and start >= 1 and start <= 30) :
		pass
	elif (level == 4 and start >= 1 and start <= 40) :
		pass
	elif (level == 5 and start >= 1 and start <= 40) :
		pass
	elif (level == 6 and start >= 1 and start <= 50) :
		pass
	else :
		return False
	return True

def printUsage() :
	print "usage unaviliable. (usage : ./genscript.py level start])"
	print "--------------------"
	print "level (1, 2, 3, 4, 5, 6)\nstart (1-20, 1-20, 1-30, 1-40, 1-40, 1-50)"
	print "--------------------"

if __name__ == '__main__' :
	if (len(sys.argv) == 3 and chkArgv(sys.argv[1], sys.argv[2])) :
		level = string.atoi(sys.argv[1])
		start = string.atoi(sys.argv[2])
		genscriptall(level, start, mapDict, mDelay, qDelay, lDelay, up, ntlevel, down, clickNum)
	else :
		printUsage()

