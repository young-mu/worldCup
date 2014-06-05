#!/usr/bin/python
#encoding=utf-8

import re

# count
countFrance = 8
# stars' names
nameFrance = {}
nameFrance[0] = '本泽马'
nameFrance[1] = '马图伊迪'
nameFrance[2] = '博格巴'
nameFrance[3] = '吉鲁'
nameFrance[4] = '里贝里'
nameFrance[5] = '埃夫拉'
nameFrance[6] = '科斯切尔尼'
nameFrance[7] = '洛里'
# regular expression
rFrance0 = nameFrance[0] + '.*?× (\d)'
rFrance0 = re.compile(rFrance0, re.S)
rFrance1 = nameFrance[1] + '.*?× (\d)'
rFrance1 = re.compile(rFrance1, re.S)
rFrance2 = nameFrance[2] + '.*?× (\d)'
rFrance2 = re.compile(rFrance2, re.S)
rFrance3 = nameFrance[3] + '.*?× (\d)'
rFrance3 = re.compile(rFrance3, re.S)
rFrance4 = nameFrance[4] + '.*?× (\d)'
rFrance4 = re.compile(rFrance4, re.S)
rFrance5 = nameFrance[5] + '.*?× (\d)'
rFrance5 = re.compile(rFrance5, re.S)
rFrance6 = nameFrance[6] + '.*?× (\d)'
rFrance6 = re.compile(rFrance6, re.S)
rFrance7 = nameFrance[7] + '.*?× (\d)'
rFrance7 = re.compile(rFrance7, re.S)
# stars' number
numFrance = {}
# stars' account
acctFrance = {}
for i in range(countFrance) :
	numFrance[i] = 0
	acctFrance[i] = []
