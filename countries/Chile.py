#!/usr/bin/python
#encoding=utf-8

import re

# count
countChile = 5
# stars' names
nameChile = {}
nameChile[0] = '费尔南德斯'
nameChile[1] = '比达尔'
nameChile[2] = '桑切斯'
nameChile[3] = '伊斯拉'
nameChile[4] = '布拉沃'
# regular expression
rChile0 = nameChile[0] + '.*?× (\d)'
rChile0 = re.compile(rChile0, re.S)
rChile1 = nameChile[1] + '.*?× (\d)'
rChile1 = re.compile(rChile1, re.S)
rChile2 = nameChile[2] + '.*?× (\d)'
rChile2 = re.compile(rChile2, re.S)
rChile3 = nameChile[3] + '.*?× (\d)'
rChile3 = re.compile(rChile3, re.S)
rChile4 = nameChile[4] + '.*?× (\d)'
rChile4 = re.compile(rChile4, re.S)
# stars' number
numChile = {}
# stars' account
acctChile = {}
for i in range(countChile) :
	numChile[i] = 0
	acctChile[i] = []
