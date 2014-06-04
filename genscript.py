#!/usr/bin/python
#encoding=utf-8

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

# script file
scriptfile = open('./script.txt', 'w+')
scriptfile.write('循环：1\r\n')

# coordinates (customed coordinates)
coordfile = open('./coord_1.txt', 'r')
coords = coordfile.readlines()
coordfile.close()
#print coords
for coordsline in coords :
	coordsline = coordsline[4:].strip('\r\n')
	coordslist = coordsline.split(', ')
	# one answer (multiple coordinates)
	for coord in coordslist :
		scriptfile.write('坐标：' + mapdict[coord] + '\r\n')
		scriptfile.write('鼠标：左键\r\n')
		scriptfile.write('延时：200\r\n')
	scriptfile.write('延时：3000\r\n')

scriptfile.close()


