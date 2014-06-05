#!/usr/bin/python
#encoding=utf-8

import re

# count
countUruguay = 5
# stars' names
nameUruguay = {}
nameUruguay[0] = '卡瓦尼'
nameUruguay[1] = '穆斯莱拉'
nameUruguay[2] = '苏亚雷斯'
nameUruguay[3] = '戈丁'
nameUruguay[4] = '迭戈・佩雷斯'
# regular expression
rUruguay0 = nameUruguay[0] + '.*?× (\d)'
rUruguay0 = re.compile(rUruguay0, re.S)
rUruguay1 = nameUruguay[1] + '.*?× (\d)'
rUruguay1 = re.compile(rUruguay1, re.S)
rUruguay2 = nameUruguay[2] + '.*?× (\d)'
rUruguay2 = re.compile(rUruguay2, re.S)
rUruguay3 = nameUruguay[3] + '.*?× (\d)'
rUruguay3 = re.compile(rUruguay3, re.S)
rUruguay4 = nameUruguay[4] + '.*?× (\d)'
rUruguay4 = re.compile(rUruguay4, re.S)
# stars' number
numUruguay = {}
# stars' account
acctUruguay = {}
for i in range(countUruguay) :
	numUruguay[i] = 0
	acctUruguay[i] = []
