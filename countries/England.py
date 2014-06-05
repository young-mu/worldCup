#!/usr/bin/python
#encoding=utf-8

import re

# count
countEngland = 8
# stars' names
nameEngland = {}
nameEngland[0] = '鲁尼'
nameEngland[1] = '兰帕德'
nameEngland[2] = '威尔希尔'
nameEngland[3] = '斯图里奇'
nameEngland[4] = '杰拉德'
nameEngland[5] = '维尔贝克'
nameEngland[6] = '贝恩斯'
nameEngland[7] = '哈特'
# regular expression
rEngland0 = nameEngland[0] + '.*?× (\d)'
rEngland0 = re.compile(rEngland0, re.S)
rEngland1 = nameEngland[1] + '.*?× (\d)'
rEngland1 = re.compile(rEngland1, re.S)
rEngland2 = nameEngland[2] + '.*?× (\d)'
rEngland2 = re.compile(rEngland2, re.S)
rEngland3 = nameEngland[3] + '.*?× (\d)'
rEngland3 = re.compile(rEngland3, re.S)
rEngland4 = nameEngland[4] + '.*?× (\d)'
rEngland4 = re.compile(rEngland4, re.S)
rEngland5 = nameEngland[5] + '.*?× (\d)'
rEngland5 = re.compile(rEngland5, re.S)
rEngland6 = nameEngland[6] + '.*?× (\d)'
rEngland6 = re.compile(rEngland6, re.S)
rEngland7 = nameEngland[7] + '.*?× (\d)'
rEngland7 = re.compile(rEngland7, re.S)
# stars' number
numEngland = {}
# stars' account
acctEngland = {}
for i in range(countEngland) :
	numEngland[i] = 0
	acctEngland[i] = []
