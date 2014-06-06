#!/usr/bin/python
#encoding=utf-8

import re

# count
countItaly = 8
# stars' names
nameItaly = {}
nameItaly[0] = '马尔基西奥'
nameItaly[1] = '德罗西'
nameItaly[2] = '巴尔扎利'
nameItaly[3] = '皮尔洛'
nameItaly[4] = '巴洛特利'
nameItaly[5] = '基耶利尼'
nameItaly[6] = '蒙托利沃'
nameItaly[7] = '布冯'
# regular expression
rItaly0 = nameItaly[0] + '.*?× (\d)'
rItaly0 = re.compile(rItaly0, re.S)
rItaly1 = nameItaly[1] + '.*?× (\d)'
rItaly1 = re.compile(rItaly1, re.S)
rItaly2 = nameItaly[2] + '.*?× (\d)'
rItaly2 = re.compile(rItaly2, re.S)
rItaly3 = nameItaly[3] + '.*?× (\d)'
rItaly3 = re.compile(rItaly3, re.S)
rItaly4 = nameItaly[4] + '.*?× (\d)'
rItaly4 = re.compile(rItaly4, re.S)
rItaly5 = nameItaly[5] + '.*?× (\d)'
rItaly5 = re.compile(rItaly5, re.S)
rItaly6 = nameItaly[6] + '.*?× (\d)'
rItaly6 = re.compile(rItaly6, re.S)
rItaly7 = nameItaly[7] + '.*?× (\d)'
rItaly7 = re.compile(rItaly7, re.S)
# stars' number
numItaly = {}
# stars' account
acctItaly = {}
for i in range(countItaly) :
	numItaly[i] = 0
	acctItaly[i] = []
