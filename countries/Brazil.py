#!/usr/bin/python
#encoding=utf-8

import re

# count
countBrazil = 8
# stars' names
nameBrazil = {}
nameBrazil[0] = '阿尔维斯'
nameBrazil[1] = '马塞洛'
nameBrazil[2] = '大卫・路易斯'
nameBrazil[3] = '奥斯卡'
nameBrazil[4] = '弗雷德'
nameBrazil[5] = '内马尔'
nameBrazil[6] = '蒂亚戈・席尔瓦'
nameBrazil[7] = '塞萨尔'
# regular expression
rBrazil0 = nameBrazil[0] + '.*?× (\d)'
rBrazil0 = re.compile(rBrazil0, re.S)
rBrazil1 = nameBrazil[1] + '.*?× (\d)'
rBrazil1 = re.compile(rBrazil1, re.S)
rBrazil2 = nameBrazil[2] + '.*?× (\d)'
rBrazil2 = re.compile(rBrazil2, re.S)
rBrazil3 = nameBrazil[3] + '.*?× (\d)'
rBrazil3 = re.compile(rBrazil3, re.S)
rBrazil4 = nameBrazil[4] + '.*?× (\d)'
rBrazil4 = re.compile(rBrazil4, re.S)
rBrazil5 = nameBrazil[5] + '.*?× (\d)'
rBrazil5 = re.compile(rBrazil5, re.S)
rBrazil6 = nameBrazil[6] + '.*?× (\d)'
rBrazil6 = re.compile(rBrazil6, re.S)
rBrazil7 = nameBrazil[7] + '.*?× (\d)'
rBrazil7 = re.compile(rBrazil7, re.S)
# stars' number
numBrazil = {}
# stars' account
acctBrazil = {}
for i in range(countBrazil) :
	numBrazil[i] = 0
	acctBrazil[i] = []
