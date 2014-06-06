#!/usr/bin/python
#encoding=utf-8

# down page 
down = '1271-750'
# next level
ntlevel = '940-730'
# up page
up = '1271-70'
# click number
clickNum = 3

# initial values
pos_11 = [432, 550]
pos_16 = [792, 550]
pos_21 = [465, 612]

# height and width of each element
width = (pos_16[0] - pos_11[0]) / 5
height = (pos_21[1] - pos_11[1])

# other elements' coordinates
pos_12 = [pos_11[0] + width, pos_11[1]]
pos_13 = [pos_11[0] + 2 * width, pos_11[1]]
pos_14 = [pos_11[0] + 3 * width, pos_11[1]]
pos_15 = [pos_11[0] + 4 * width, pos_11[1]]
pos_22 = [pos_21[0] + width, pos_21[1]]
pos_23 = [pos_21[0] + 2 * width, pos_21[1]]
pos_24 = [pos_21[0] + 3 * width, pos_21[1]]
pos_25 = [pos_21[0] + 4 * width, pos_21[1]]
pos_26 = [pos_21[0] + 5 * width, pos_21[1]]
pos_31 = [pos_11[0], pos_11[1] + 2 * height]
pos_32 = [pos_12[0], pos_12[1] + 2 * height]
pos_33 = [pos_13[0], pos_13[1] + 2 * height]
pos_34 = [pos_14[0], pos_14[1] + 2 * height]
pos_35 = [pos_15[0], pos_15[1] + 2 * height]
pos_36 = [pos_16[0], pos_16[1] + 2 * height]

def keyCoord(pos_coord) :
	return str(pos_coord[0]) + '-' + str(pos_coord[1])

# mapDict
mapDict = {}
mapDict['11'] = keyCoord(pos_11)
mapDict['12'] = keyCoord(pos_12)
mapDict['13'] = keyCoord(pos_13)
mapDict['14'] = keyCoord(pos_14)
mapDict['15'] = keyCoord(pos_15)
mapDict['16'] = keyCoord(pos_16)
mapDict['21'] = keyCoord(pos_21)
mapDict['22'] = keyCoord(pos_22)
mapDict['23'] = keyCoord(pos_23)
mapDict['24'] = keyCoord(pos_24)
mapDict['25'] = keyCoord(pos_25)
mapDict['26'] = keyCoord(pos_26)
mapDict['31'] = keyCoord(pos_31)
mapDict['32'] = keyCoord(pos_32)
mapDict['33'] = keyCoord(pos_33)
mapDict['34'] = keyCoord(pos_34)
mapDict['35'] = keyCoord(pos_35)
mapDict['36'] = keyCoord(pos_36)
