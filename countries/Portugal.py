#!/usr/bin/python
#encoding=utf-8

import re

# count
countPortugal = 8
# stars' names
namePortugal = {}
namePortugal[0] = '维洛索'
namePortugal[1] = '纳尼'
namePortugal[2] = 'C罗'
namePortugal[3] = '佩佩'
namePortugal[4] = '科恩特朗'
namePortugal[5] = '穆蒂尼奥'
namePortugal[6] = '布鲁诺・阿尔维斯'
namePortugal[7] = '梅雷莱斯'
# regular expression
rPortugal0 = namePortugal[0] + '.*?× (\d)'
rPortugal0 = re.compile(rPortugal0, re.S)
rPortugal1 = namePortugal[1] + '.*?× (\d)'
rPortugal1 = re.compile(rPortugal1, re.S)
rPortugal2 = namePortugal[2] + '.*?× (\d)'
rPortugal2 = re.compile(rPortugal2, re.S)
rPortugal3 = namePortugal[3] + '.*?× (\d)'
rPortugal3 = re.compile(rPortugal3, re.S)
rPortugal4 = namePortugal[4] + '.*?× (\d)'
rPortugal4 = re.compile(rPortugal4, re.S)
rPortugal5 = namePortugal[5] + '.*?× (\d)'
rPortugal5 = re.compile(rPortugal5, re.S)
rPortugal6 = namePortugal[6] + '.*?× (\d)'
rPortugal6 = re.compile(rPortugal6, re.S)
rPortugal7 = namePortugal[7] + '.*?× (\d)'
rPortugal7 = re.compile(rPortugal7, re.S)
# stars' number
numPortugal = {}
# stars' account
acctPortugal = {}
for i in range(countPortugal) :
	numPortugal[i] = 0
	acctPortugal[i] = []
