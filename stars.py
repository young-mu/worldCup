#!/usr/bin/python
#encoding=utf-8

import re, string

starsFile = r'./mycopy.txt'
starsFile = open(starsFile, 'r')
starsCtx = starsFile.read()
starsCtx = unicode(starsCtx, 'gb2312').encode('utf-8')

# split into multiple accounts' context
rSplit = re.compile(r"(.*?反馈信息举报)", re.S)
acctCtx = re.findall(rSplit, starsCtx)

rAccount = re.compile(r"(.*?)退出球星卡")
# Spain
nameSpain = {}
nameSpain[0] = '卡西利亚斯'
nameSpain[1] = '皮克'
nameSpain[2] = '拉莫斯'
nameSpain[3] = '伊涅斯塔'
nameSpain[4] = '哈维'
nameSpain[5] = '法布雷加斯'
nameSpain[6] = '大卫・席尔瓦'
nameSpain[7] = '迭戈・科斯塔'
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
numSpain = {}
acctSpain = {}
for i in range(8) :
	numSpain[i] = 0
	acctSpain[i] = []
# Brazil


for i in range(len(acctCtx)) :
	account = re.findall(rAccount, acctCtx[i])
	# Spain
	Spain = []
	Spain.append(re.findall(rSpain0, acctCtx[i]))
	Spain.append(re.findall(rSpain1, acctCtx[i]))
	Spain.append(re.findall(rSpain2, acctCtx[i]))
	Spain.append(re.findall(rSpain3, acctCtx[i]))
	Spain.append(re.findall(rSpain4, acctCtx[i]))
	Spain.append(re.findall(rSpain5, acctCtx[i]))
	Spain.append(re.findall(rSpain6, acctCtx[i]))
	Spain.append(re.findall(rSpain7, acctCtx[i]))
	for i in range(8) :
		if Spain[i][0] >= 1 :
			numSpain[i] += string.atoi(Spain[i][0])
			acctSpain[i].append(account) 

for i in range(8) :
	print nameSpain[i] + ' : ' + str(numSpain[i])
