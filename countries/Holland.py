#!/usr/bin/python
#encoding=utf-8

import re

# count
countHolland = 8
# stars' names
nameHolland = {}
nameHolland[0] = '库伊特'
nameHolland[1] = '范德法特'
nameHolland[2] = '范佩西'
nameHolland[3] = '罗本'
nameHolland[4] = '斯内德'
nameHolland[5] = '亨特拉尔'
nameHolland[6] = '德容'
nameHolland[7] = '弗拉尔'
# regular expression
rHolland0 = nameHolland[0] + '.*?× (\d)'
rHolland0 = re.compile(rHolland0, re.S)
rHolland1 = nameHolland[1] + '.*?× (\d)'
rHolland1 = re.compile(rHolland1, re.S)
rHolland2 = nameHolland[2] + '.*?× (\d)'
rHolland2 = re.compile(rHolland2, re.S)
rHolland3 = nameHolland[3] + '.*?× (\d)'
rHolland3 = re.compile(rHolland3, re.S)
rHolland4 = nameHolland[4] + '.*?× (\d)'
rHolland4 = re.compile(rHolland4, re.S)
rHolland5 = nameHolland[5] + '.*?× (\d)'
rHolland5 = re.compile(rHolland5, re.S)
rHolland6 = nameHolland[6] + '.*?× (\d)'
rHolland6 = re.compile(rHolland6, re.S)
rHolland7 = nameHolland[7] + '.*?× (\d)'
rHolland7 = re.compile(rHolland7, re.S)
# stars' number
numHolland = {}
# stars' account
acctHolland = {}
for i in range(countHolland) :
	numHolland[i] = 0
	acctHolland[i] = []
