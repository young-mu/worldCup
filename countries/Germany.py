#!/usr/bin/python
#encoding=utf-8

import re

# count
countGermany = 8
# stars' names
nameGermany = {}
nameGermany[0] = '罗伊斯'
nameGermany[1] = '施魏因斯泰格'
nameGermany[2] = '厄齐尔'
nameGermany[3] = '拉姆'
nameGermany[4] = '格策'
nameGermany[5] = '穆勒'
nameGermany[6] = '克洛泽'
nameGermany[7] = '诺伊尔'
# regular expression
rGermany0 = nameGermany[0] + '.*?× (\d)'
rGermany0 = re.compile(rGermany0, re.S)
rGermany1 = nameGermany[1] + '.*?× (\d)'
rGermany1 = re.compile(rGermany1, re.S)
rGermany2 = nameGermany[2] + '.*?× (\d)'
rGermany2 = re.compile(rGermany2, re.S)
rGermany3 = nameGermany[3] + '.*?× (\d)'
rGermany3 = re.compile(rGermany3, re.S)
rGermany4 = nameGermany[4] + '.*?× (\d)'
rGermany4 = re.compile(rGermany4, re.S)
rGermany5 = nameGermany[5] + '.*?× (\d)'
rGermany5 = re.compile(rGermany5, re.S)
rGermany6 = nameGermany[6] + '.*?× (\d)'
rGermany6 = re.compile(rGermany6, re.S)
rGermany7 = nameGermany[7] + '.*?× (\d)'
rGermany7 = re.compile(rGermany7, re.S)
# stars' number
numGermany = {}
# stars' account
acctGermany = {}
for i in range(countGermany) :
	numGermany[i] = 0
	acctGermany[i] = []
