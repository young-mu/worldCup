#!/usr/bin/python
#encoding=utf-8

import re

# count
countAllstar = 8
# stars' names
nameAllstar = {}
nameAllstar[0] = '埃托奥'
nameAllstar[1] = '德罗巴'
nameAllstar[2] = '亚亚・图雷'
nameAllstar[3] = '米克尔'
nameAllstar[4] = '埃尔南德斯'
nameAllstar[5] = '法尔考'
nameAllstar[6] = '哲科'
nameAllstar[7] = '利希施泰纳'
# regular expression
rAllstar0 = nameAllstar[0] + '.*?× (\d)'
rAllstar0 = re.compile(rAllstar0, re.S)
rAllstar1 = nameAllstar[1] + '.*?× (\d)'
rAllstar1 = re.compile(rAllstar1, re.S)
rAllstar2 = nameAllstar[2] + '.*?× (\d)'
rAllstar2 = re.compile(rAllstar2, re.S)
rAllstar3 = nameAllstar[3] + '.*?× (\d)'
rAllstar3 = re.compile(rAllstar3, re.S)
rAllstar4 = nameAllstar[4] + '.*?× (\d)'
rAllstar4 = re.compile(rAllstar4, re.S)
rAllstar5 = nameAllstar[5] + '.*?× (\d)'
rAllstar5 = re.compile(rAllstar5, re.S)
rAllstar6 = nameAllstar[6] + '.*?× (\d)'
rAllstar6 = re.compile(rAllstar6, re.S)
rAllstar7 = nameAllstar[7] + '.*?× (\d)'
rAllstar7 = re.compile(rAllstar7, re.S)
# stars' number
numAllstar = {}
# stars' account
acctAllstar = {}
for i in range(countAllstar) :
	numAllstar[i] = 0
	acctAllstar[i] = []
