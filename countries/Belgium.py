#!/usr/bin/python
#encoding=utf-8

import re

# count
countBelgium = 5
# stars' names
nameBelgium = {}
nameBelgium[0] = '卢卡库'
nameBelgium[1] = '阿扎尔'
nameBelgium[2] = '孔帕尼'
nameBelgium[3] = '费莱尼'
nameBelgium[4] = '费尔马伦'
# regular expression
rBelgium0 = nameBelgium[0] + '.*?× (\d)'
rBelgium0 = re.compile(rBelgium0, re.S)
rBelgium1 = nameBelgium[1] + '.*?× (\d)'
rBelgium1 = re.compile(rBelgium1, re.S)
rBelgium2 = nameBelgium[2] + '.*?× (\d)'
rBelgium2 = re.compile(rBelgium2, re.S)
rBelgium3 = nameBelgium[3] + '.*?× (\d)'
rBelgium3 = re.compile(rBelgium3, re.S)
rBelgium4 = nameBelgium[4] + '.*?× (\d)'
rBelgium4 = re.compile(rBelgium4, re.S)
# stars' number
numBelgium = {}
# stars' account
acctBelgium = {}
for i in range(countBelgium) :
	numBelgium[i] = 0
	acctBelgium[i] = []
