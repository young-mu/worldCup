#!/usr/bin/python
#encoding=utf-8

import re

# count
countJapan = 5
# stars' names
nameJapan = {}
nameJapan[0] = '本田圭佑'
nameJapan[1] = '香川真司'
nameJapan[2] = '长友佑都'
nameJapan[3] = '冈崎慎司'
nameJapan[4] = '内田笃人'
# regular expression
rJapan0 = nameJapan[0] + '.*?× (\d)'
rJapan0 = re.compile(rJapan0, re.S)
rJapan1 = nameJapan[1] + '.*?× (\d)'
rJapan1 = re.compile(rJapan1, re.S)
rJapan2 = nameJapan[2] + '.*?× (\d)'
rJapan2 = re.compile(rJapan2, re.S)
rJapan3 = nameJapan[3] + '.*?× (\d)'
rJapan3 = re.compile(rJapan3, re.S)
rJapan4 = nameJapan[4] + '.*?× (\d)'
rJapan4 = re.compile(rJapan4, re.S)
# stars' number
numJapan = {}
# stars' account
acctJapan = {}
for i in range(countJapan) :
	numJapan[i] = 0
	acctJapan[i] = []
