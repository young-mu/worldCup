#!/usr/bin/python
#encoding=utf-8

import re

# count
countArgentina = 8
# stars' names
nameArgentina = {}
nameArgentina[0] = '梅西'
nameArgentina[1] = '拉维奇'
nameArgentina[2] = '阿奎罗'
nameArgentina[3] = '伊瓜因'
nameArgentina[4] = '帕拉西奥'
nameArgentina[5] = '马斯切拉诺'
nameArgentina[6] = '迪马利亚'
nameArgentina[7] = '萨巴莱塔'
# regular expression
rArgentina0 = nameArgentina[0] + '.*?× (\d)'
rArgentina0 = re.compile(rArgentina0, re.S)
rArgentina1 = nameArgentina[1] + '.*?× (\d)'
rArgentina1 = re.compile(rArgentina1, re.S)
rArgentina2 = nameArgentina[2] + '.*?× (\d)'
rArgentina2 = re.compile(rArgentina2, re.S)
rArgentina3 = nameArgentina[3] + '.*?× (\d)'
rArgentina3 = re.compile(rArgentina3, re.S)
rArgentina4 = nameArgentina[4] + '.*?× (\d)'
rArgentina4 = re.compile(rArgentina4, re.S)
rArgentina5 = nameArgentina[5] + '.*?× (\d)'
rArgentina5 = re.compile(rArgentina5, re.S)
rArgentina6 = nameArgentina[6] + '.*?× (\d)'
rArgentina6 = re.compile(rArgentina6, re.S)
rArgentina7 = nameArgentina[7] + '.*?× (\d)'
rArgentina7 = re.compile(rArgentina7, re.S)
# stars' number
numArgentina = {}
# stars' account
acctArgentina = {}
for i in range(countArgentina) :
	numArgentina[i] = 0
	acctArgentina[i] = []
