#!/usr/bin/python
#encoding=utf-8

import re

# count
countKorea = 5
# stars' names
nameKorea = {}
nameKorea[0] = '孙兴民'
nameKorea[1] = '金英权'
nameKorea[2] = '奇诚庸'
nameKorea[3] = '朴周永'
nameKorea[4] = '具滋哲'
# regular expression
rKorea0 = nameKorea[0] + '.*?× (\d)'
rKorea0 = re.compile(rKorea0, re.S)
rKorea1 = nameKorea[1] + '.*?× (\d)'
rKorea1 = re.compile(rKorea1, re.S)
rKorea2 = nameKorea[2] + '.*?× (\d)'
rKorea2 = re.compile(rKorea2, re.S)
rKorea3 = nameKorea[3] + '.*?× (\d)'
rKorea3 = re.compile(rKorea3, re.S)
rKorea4 = nameKorea[4] + '.*?× (\d)'
rKorea4 = re.compile(rKorea4, re.S)
# stars' number
numKorea = {}
# stars' account
acctKorea = {}
for i in range(countKorea) :
	numKorea[i] = 0
	acctKorea[i] = []
