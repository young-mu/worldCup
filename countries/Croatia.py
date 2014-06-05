#!/usr/bin/python
#encoding=utf-8

import re

# count
countCroatia = 5
# stars' names
nameCroatia = {}
nameCroatia[0] = '奥利奇'
nameCroatia[1] = '莫德里奇'
nameCroatia[2] = '曼祖基奇'
nameCroatia[3] = '斯尔纳'
nameCroatia[4] = '拉基蒂奇'
# regular expression
rCroatia0 = nameCroatia[0] + '.*?× (\d)'
rCroatia0 = re.compile(rCroatia0, re.S)
rCroatia1 = nameCroatia[1] + '.*?× (\d)'
rCroatia1 = re.compile(rCroatia1, re.S)
rCroatia2 = nameCroatia[2] + '.*?× (\d)'
rCroatia2 = re.compile(rCroatia2, re.S)
rCroatia3 = nameCroatia[3] + '.*?× (\d)'
rCroatia3 = re.compile(rCroatia3, re.S)
rCroatia4 = nameCroatia[4] + '.*?× (\d)'
rCroatia4 = re.compile(rCroatia4, re.S)
# stars' number
numCroatia = {}
# stars' account
acctCroatia = {}
for i in range(countCroatia) :
	numCroatia[i] = 0
	acctCroatia[i] = []
