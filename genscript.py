#!/usr/bin/python
#encoding=utf-8

import sys, string

# mouse delay
mDelay = 300
# question delay
qDelay = 2000
# level delay
lDelay = 2000

def getmapdict() :
	# coordinate mapping (map customed coordinates to screen coordinates) 
	mapfile = open('./coordmap.txt', 'r')
	maps = mapfile.readlines()
	mapfile.close()
	# generate mapping dict
	mapdict = {}
	for mapline in maps :
		mapline = mapline.strip('\r\n')
		maplist = mapline.split(' : ')
		mapdict[maplist[0]] = maplist[1]
	return mapdict

def genscript(level, mapdict, mDelay, qDelay) :
	# script file
	scriptfile = './scripts/script_' + str(level) + '.txt'
	scriptfile = open(scriptfile, 'w+')
	scriptfile.write('循环：1\r\n')
	# customed coordinates file
	coordfile = './coordinates/coord_' + str(level) + '.txt'
	coordfile = open(coordfile, 'r')
	coords = coordfile.readlines()
	coordfile.close()
	for coordsline in coords :
		coordsline = coordsline[4:].strip('\r\n')
		coordslist = coordsline.split(', ')
		# one answer includes multiple coordinates
		for coord in coordslist :
			scriptfile.write('坐标：' + mapdict[coord] + '\r\n')
			scriptfile.write('鼠标：左键\r\n')
			scriptfile.write('延时：' + str(mDelay) + '\r\n')
		scriptfile.write('延时：' + str(qDelay) + '\r\n')
	scriptfile.close()

def genscriptall(start, end, mapdict, mDelay, qDelay, lDelay) :
	assert type(start) == int
	assert type(end) == int
	assert type(mapdict) == dict
	assert type(qDelay) == int
	for idx in range(start, end + 1, 1) :
		genscript(idx, mapdict, mDelay, qDelay)
	# script file
	scriptfile = './scripts/script_all.txt'
	scriptfile = open(scriptfile, 'w+')
	scriptfile.write('循环：1\r\n')
	for idx in range(start, end + 1, 1) :
		tmpfile = './scripts/script_' + str(idx) + '.txt'
		tmpfile = open(tmpfile, 'r')
		discard = tmpfile.readline()
		scripts = tmpfile.readlines()
		for scriptline in scripts :
			scriptfile.write(scriptline)
		# page down
		scriptfile.write('坐标: 1271-750\r\n')
		for i in range(3) :
			scriptfile.write('鼠标：左键\r\n')
			scriptfile.write('延时：' + str(mDelay) + '\r\n')
		scriptfile.write('延时：' + str(mDelay) + '\r\n')
		# next game level
		scriptfile.write('延时：' + str(lDelay) + '\r\n')
		scriptfile.write('坐标：940-730\r\n')
		scriptfile.write('鼠标：左键\r\n')
		scriptfile.write('延时：' + str(mDelay) + '\r\n')
		# page up
		scriptfile.write('坐标：1271-70\r\n')
		for i in range(3) :
			scriptfile.write('鼠标：左键\r\n')
			scriptfile.write('延时：' + str(mDelay) + '\r\n')
		scriptfile.write('延时：' + str(mDelay) + '\r\n')
	scriptfile.close()	

def printUsage() :
	print "usage unaviliable. (usage : ./genscript.py [1|2|3|4|5|6|a start end])"
	print "--------------------"
	print "1~6 - 1~6 game level\na start end - multiple levels from start to end"
	print "--------------------"

if __name__ == '__main__' :
	mapdict = getmapdict()
	if (len(sys.argv) == 2 and sys.argv[1] == '1') :
		genscript(1, mapdict, mDelay, qDelay)
	elif (len(sys.argv) == 2 and sys.argv[1] == '2') :
		genscript(2, mapdict, mDelay, qDelay)
	elif (len(sys.argv) == 2 and sys.argv[1] == '3') :
		genscript(3, mapdict, mDelay, qDelay)
	elif (len(sys.argv) == 2 and sys.argv[1] == '4') :
		genscript(4, mapdict, mDelay, qDelay)
	elif (len(sys.argv) == 2 and sys.argv[1] == '5') :
		genscript(5, mapdict, mDelay, qDelay)
	elif (len(sys.argv) == 2 and sys.argv[1] == '6') :
		genscript(6, mapdict, mDelay, qDelay)
	elif (len(sys.argv) == 4 and sys.argv[1] == 'a') :
		start = string.atoi(sys.argv[2])
		end = string.atoi(sys.argv[3])
		if (start <= end and start <=6 and start >= 1 and end <= 6 and end >= 1) :
			genscriptall(start, end, mapdict, mDelay, qDelay, lDelay)
		else :
			print "unaviliable start and end."
	else :
		printUsage()

