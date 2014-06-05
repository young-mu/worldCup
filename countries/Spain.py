#!/usr/bin/python
#encoding=utf-8

import re

# count
countSpain = 8
# stars' names
nameSpain = {}
nameSpain[0] = '卡西利亚斯'
nameSpain[1] = '皮克'
nameSpain[2] = '拉莫斯'
nameSpain[3] = '伊涅斯塔'
nameSpain[4] = '哈维'
nameSpain[5] = '法布雷加斯'
nameSpain[6] = '大卫・席尔瓦'
nameSpain[7] = '迭戈・科斯塔'
# regular expression
rSpain0 = nameSpain[0] + '.*?× (\d)'
rSpain0 = re.compile(rSpain0, re.S)
rSpain1 = nameSpain[1] + '.*?× (\d)'
rSpain1 = re.compile(rSpain1, re.S)
rSpain2 = nameSpain[2] + '.*?× (\d)'
rSpain2 = re.compile(rSpain2, re.S)
rSpain3 = nameSpain[3] + '.*?× (\d)'
rSpain3 = re.compile(rSpain3, re.S)
rSpain4 = nameSpain[4] + '.*?× (\d)'
rSpain4 = re.compile(rSpain4, re.S)
rSpain5 = nameSpain[5] + '.*?× (\d)'
rSpain5 = re.compile(rSpain5, re.S)
rSpain6 = nameSpain[6] + '.*?× (\d)'
rSpain6 = re.compile(rSpain6, re.S)
rSpain7 = nameSpain[7] + '.*?× (\d)'
rSpain7 = re.compile(rSpain7, re.S)
# stars' number
numSpain = {}
# stars' account
acctSpain = {}
for i in range(countSpain) :
	numSpain[i] = 0
	acctSpain[i] = []
