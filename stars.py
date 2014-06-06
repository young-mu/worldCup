#!/usr/bin/python
#encoding=utf-8

import re, sys, string

sys.path.append("./countries")
from Spain import *
from Brazil import *
from Germany import *
from Argentina import *
from England import *
from Italy import *
from France import *
from Portugal import *
from Holland import *
from Allstar import *
from Uruguay import *
from Belgium import *
from Croatia import *
from Chile import *
from Japan import *
from Korea import *

starsFile = r'./allstars.txt'
starsFile = open(starsFile, 'r')
starsCtx = starsFile.read()
starsCtx = unicode(starsCtx, 'gb2312').encode('utf-8')

# split into multiple accounts' context
rSplit = re.compile(r"(.*?反馈信息举报\r\n)", re.S)
acctCtx = re.findall(rSplit, starsCtx)
# remove repeated elements (the same accounts)
acctCtx = list(set(acctCtx))
# account regular expression
rAccount = re.compile(r"(.*?)退出球星卡")
accountList = []

for i in range(len(acctCtx)) :
	account = re.findall(rAccount, acctCtx[i])
	accountList.append(account[0])
	# 1. Spain
	Spain = []
	Spain.append(re.findall(rSpain0, acctCtx[i]))
	Spain.append(re.findall(rSpain1, acctCtx[i]))
	Spain.append(re.findall(rSpain2, acctCtx[i]))
	Spain.append(re.findall(rSpain3, acctCtx[i]))
	Spain.append(re.findall(rSpain4, acctCtx[i]))
	Spain.append(re.findall(rSpain5, acctCtx[i]))
	Spain.append(re.findall(rSpain6, acctCtx[i]))
	Spain.append(re.findall(rSpain7, acctCtx[i]))
	for j in range(countSpain) :
		num = string.atoi(Spain[j][0])
		if num >= 1 :
			numSpain[j] += num 
			for k in range(num) :
				acctSpain[j].append(account[0]) 
	# 2. Brazil
	Brazil = []
	Brazil.append(re.findall(rBrazil0, acctCtx[i]))
	Brazil.append(re.findall(rBrazil1, acctCtx[i]))
	Brazil.append(re.findall(rBrazil2, acctCtx[i]))
	Brazil.append(re.findall(rBrazil3, acctCtx[i]))
	Brazil.append(re.findall(rBrazil4, acctCtx[i]))
	Brazil.append(re.findall(rBrazil5, acctCtx[i]))
	Brazil.append(re.findall(rBrazil6, acctCtx[i]))
	Brazil.append(re.findall(rBrazil7, acctCtx[i]))
	for j in range(countBrazil) :
		num = string.atoi(Brazil[j][0])
		if num >= 1 :
			numBrazil[j] += num 
			for k in range(num) :
				acctBrazil[j].append(account[0]) 
	# 3. Germany
	Germany = []
	Germany.append(re.findall(rGermany0, acctCtx[i]))
	Germany.append(re.findall(rGermany1, acctCtx[i]))
	Germany.append(re.findall(rGermany2, acctCtx[i]))
	Germany.append(re.findall(rGermany3, acctCtx[i]))
	Germany.append(re.findall(rGermany4, acctCtx[i]))
	Germany.append(re.findall(rGermany5, acctCtx[i]))
	Germany.append(re.findall(rGermany6, acctCtx[i]))
	Germany.append(re.findall(rGermany7, acctCtx[i]))
	for j in range(countGermany) :
		num = string.atoi(Germany[j][0])
		if num >= 1 :
			numGermany[j] += num
			for k in range(num) :
				acctGermany[j].append(account[0]) 
	# 4. Argentina
	Argentina = []
	Argentina.append(re.findall(rArgentina0, acctCtx[i]))
	Argentina.append(re.findall(rArgentina1, acctCtx[i]))
	Argentina.append(re.findall(rArgentina2, acctCtx[i]))
	Argentina.append(re.findall(rArgentina3, acctCtx[i]))
	Argentina.append(re.findall(rArgentina4, acctCtx[i]))
	Argentina.append(re.findall(rArgentina5, acctCtx[i]))
	Argentina.append(re.findall(rArgentina6, acctCtx[i]))
	Argentina.append(re.findall(rArgentina7, acctCtx[i]))
	for j in range(countArgentina) :
		num = string.atoi(Argentina[j][0])
		if num >= 1 :
			numArgentina[j] += num 
			for k in range(num) :
				acctArgentina[j].append(account[0]) 
	# 5. England
	England = []
	England.append(re.findall(rEngland0, acctCtx[i]))
	England.append(re.findall(rEngland1, acctCtx[i]))
	England.append(re.findall(rEngland2, acctCtx[i]))
	England.append(re.findall(rEngland3, acctCtx[i]))
	England.append(re.findall(rEngland4, acctCtx[i]))
	England.append(re.findall(rEngland5, acctCtx[i]))
	England.append(re.findall(rEngland6, acctCtx[i]))
	England.append(re.findall(rEngland7, acctCtx[i]))
	for j in range(countEngland) :
		num = string.atoi(England[j][0])
		if num >= 1 :
			numEngland[j] += num 
			for k in range(num) :
				acctEngland[j].append(account[0]) 
	# 6. Italy
	Italy = []
	Italy.append(re.findall(rItaly0, acctCtx[i]))
	Italy.append(re.findall(rItaly1, acctCtx[i]))
	Italy.append(re.findall(rItaly2, acctCtx[i]))
	Italy.append(re.findall(rItaly3, acctCtx[i]))
	Italy.append(re.findall(rItaly4, acctCtx[i]))
	Italy.append(re.findall(rItaly5, acctCtx[i]))
	Italy.append(re.findall(rItaly6, acctCtx[i]))
	Italy.append(re.findall(rItaly7, acctCtx[i]))
	for j in range(countItaly) :
		num = string.atoi(Italy[j][0])
		if num >= 1 :
			numItaly[j] += num 
			for k in range(num) :
				acctItaly[j].append(account[0]) 
	# 7. France
	France = []
	France.append(re.findall(rFrance0, acctCtx[i]))
	France.append(re.findall(rFrance1, acctCtx[i]))
	France.append(re.findall(rFrance2, acctCtx[i]))
	France.append(re.findall(rFrance3, acctCtx[i]))
	France.append(re.findall(rFrance4, acctCtx[i]))
	France.append(re.findall(rFrance5, acctCtx[i]))
	France.append(re.findall(rFrance6, acctCtx[i]))
	France.append(re.findall(rFrance7, acctCtx[i]))
	for j in range(countFrance) :
		num = string.atoi(France[j][0])
		if num >= 1 :
			numFrance[j] += num 
			for k in range(num) :
				acctFrance[j].append(account[0]) 
	# 8. Portugal
	Portugal = []
	Portugal.append(re.findall(rPortugal0, acctCtx[i]))
	Portugal.append(re.findall(rPortugal1, acctCtx[i]))
	Portugal.append(re.findall(rPortugal2, acctCtx[i]))
	Portugal.append(re.findall(rPortugal3, acctCtx[i]))
	Portugal.append(re.findall(rPortugal4, acctCtx[i]))
	Portugal.append(re.findall(rPortugal5, acctCtx[i]))
	Portugal.append(re.findall(rPortugal6, acctCtx[i]))
	Portugal.append(re.findall(rPortugal7, acctCtx[i]))
	for j in range(countPortugal) :
		num = string.atoi(Portugal[j][0])
		if num >= 1 :
			numPortugal[j] += num 
			for k in range(num) :
				acctPortugal[j].append(account[0]) 
	# 9. Holland
	Holland = []
	Holland.append(re.findall(rHolland0, acctCtx[i]))
	Holland.append(re.findall(rHolland1, acctCtx[i]))
	Holland.append(re.findall(rHolland2, acctCtx[i]))
	Holland.append(re.findall(rHolland3, acctCtx[i]))
	Holland.append(re.findall(rHolland4, acctCtx[i]))
	Holland.append(re.findall(rHolland5, acctCtx[i]))
	Holland.append(re.findall(rHolland6, acctCtx[i]))
	Holland.append(re.findall(rHolland7, acctCtx[i]))
	for j in range(countHolland) :
		num = string.atoi(Holland[j][0])
		if num >= 1 :
			numHolland[j] += num
			for k in range(num) :
				acctHolland[j].append(account[0]) 
	# 10. Allstar
	Allstar = []
	Allstar.append(re.findall(rAllstar0, acctCtx[i]))
	Allstar.append(re.findall(rAllstar1, acctCtx[i]))
	Allstar.append(re.findall(rAllstar2, acctCtx[i]))
	Allstar.append(re.findall(rAllstar3, acctCtx[i]))
	Allstar.append(re.findall(rAllstar4, acctCtx[i]))
	Allstar.append(re.findall(rAllstar5, acctCtx[i]))
	Allstar.append(re.findall(rAllstar6, acctCtx[i]))
	Allstar.append(re.findall(rAllstar7, acctCtx[i]))
	for j in range(countAllstar) :
		num = string.atoi(Allstar[j][0])
		if num >= 1 :
			numAllstar[j] += num 
			for k in range(num) :
				acctAllstar[j].append(account[0]) 
	# 11. Uruguay
	Uruguay = []
	Uruguay.append(re.findall(rUruguay0, acctCtx[i]))
	Uruguay.append(re.findall(rUruguay1, acctCtx[i]))
	Uruguay.append(re.findall(rUruguay2, acctCtx[i]))
	Uruguay.append(re.findall(rUruguay3, acctCtx[i]))
	Uruguay.append(re.findall(rUruguay4, acctCtx[i]))
	for j in range(countUruguay) :
		num = string.atoi(Uruguay[j][0])
		if string.atoi(Uruguay[j][0]) >= 1 :
			numUruguay[j] += num
			for k in range(num) :
				acctUruguay[j].append(account[0]) 
	# 12. Belgium
	Belgium = []
	Belgium.append(re.findall(rBelgium0, acctCtx[i]))
	Belgium.append(re.findall(rBelgium1, acctCtx[i]))
	Belgium.append(re.findall(rBelgium2, acctCtx[i]))
	Belgium.append(re.findall(rBelgium3, acctCtx[i]))
	Belgium.append(re.findall(rBelgium4, acctCtx[i]))
	for j in range(countBelgium) :
		num = string.atoi(Belgium[j][0])
		if num >= 1 :
			numBelgium[j] += num
			for k in range(num) :
				acctBelgium[j].append(account[0]) 
	# 13. Croatia
	Croatia = []
	Croatia.append(re.findall(rCroatia0, acctCtx[i]))
	Croatia.append(re.findall(rCroatia1, acctCtx[i]))
	Croatia.append(re.findall(rCroatia2, acctCtx[i]))
	Croatia.append(re.findall(rCroatia3, acctCtx[i]))
	Croatia.append(re.findall(rCroatia4, acctCtx[i]))
	for j in range(countCroatia) :
		num = string.atoi(Croatia[j][0])
		if num >= 1 :
			numCroatia[j] += num
			for k in range(num) :
				acctCroatia[j].append(account[0]) 
	# 14. Chile
	Chile = []
	Chile.append(re.findall(rChile0, acctCtx[i]))
	Chile.append(re.findall(rChile1, acctCtx[i]))
	Chile.append(re.findall(rChile2, acctCtx[i]))
	Chile.append(re.findall(rChile3, acctCtx[i]))
	Chile.append(re.findall(rChile4, acctCtx[i]))
	for j in range(countChile) :
		num = string.atoi(Chile[j][0])
		if num >= 1 :
			numChile[j] += num
			for k in range(num) :
				acctChile[j].append(account[0]) 
	# 15. Japan
	Japan = []
	Japan.append(re.findall(rJapan0, acctCtx[i]))
	Japan.append(re.findall(rJapan1, acctCtx[i]))
	Japan.append(re.findall(rJapan2, acctCtx[i]))
	Japan.append(re.findall(rJapan3, acctCtx[i]))
	Japan.append(re.findall(rJapan4, acctCtx[i]))
	for j in range(countJapan) :
		num = string.atoi(Japan[j][0])
		if num >= 1 :
			numJapan[j] += num 
			for k in range(num) :
				acctJapan[j].append(account[0]) 
	# 16. Korea
	Korea = []
	Korea.append(re.findall(rKorea0, acctCtx[i]))
	Korea.append(re.findall(rKorea1, acctCtx[i]))
	Korea.append(re.findall(rKorea2, acctCtx[i]))
	Korea.append(re.findall(rKorea3, acctCtx[i]))
	Korea.append(re.findall(rKorea4, acctCtx[i]))
	for j in range(countKorea) :
		num = string.atoi(Korea[j][0])
		if num >= 1 :
			numKorea[j] += num
			for k in range(num) :
				acctKorea[j].append(account[0]) 

if __name__ == '__main__' :
	print '---------- accounts ----------'
	print accountList
	print '---------- 1. Spain ----------'
	for i in range(countSpain) :
		namenum = '%s (%d)' %(nameSpain[i], numSpain[i])
		print namenum.ljust(25) + '\t\t' + str(acctSpain[i])
	print '---------- 2. Brazil ----------'
	for i in range(countBrazil) :
		namenum = '%s (%d)' %(nameBrazil[i], numBrazil[i])
		print namenum.ljust(25) + '\t\t' + str(acctBrazil[i])
	print '---------- 3. Germany  ----------'
	for i in range(countGermany) :
		namenum = '%s (%d)' %(nameGermany[i], numGermany[i])
		print namenum.ljust(25) + '\t\t' + str(acctGermany[i])
	print '---------- 4. Argentina ----------'
	for i in range(countArgentina) :
		namenum = '%s (%d)' %(nameArgentina[i], numArgentina[i])
		print namenum.ljust(25) + '\t\t' + str(acctArgentina[i])
	print '---------- 5. England ----------'
	for i in range(countEngland) :
		namenum = '%s (%d)' %(nameEngland[i], numEngland[i])
		print namenum.ljust(25) + '\t\t' + str(acctEngland[i])
	print '---------- 6. Italy ----------'
	for i in range(countItaly) :
		namenum = '%s (%d)' %(nameItaly[i], numItaly[i])
		print namenum.ljust(25) + '\t\t' + str(acctItaly[i])
	print '---------- 7. France ----------'
	for i in range(countFrance) :
		namenum = '%s (%d)' %(nameFrance[i], numFrance[i])
		print namenum.ljust(25) + '\t\t' + str(acctFrance[i])
	print '---------- 8. Portugal ----------'
	for i in range(countPortugal) :
		namenum = '%s (%d)' %(namePortugal[i], numPortugal[i])
		print namenum.ljust(20) + '\t\t' + str(acctPortugal[i])
	print '---------- 9. Holland ----------'
	for i in range(countHolland) :
		namenum = '%s (%d)' %(nameHolland[i], numHolland[i])
		print namenum.ljust(25) + '\t\t' + str(acctHolland[i])
	print '---------- 10. Allstar ----------'
	for i in range(countAllstar) :
		namenum = '%s (%d)' %(nameAllstar[i], numAllstar[i])
		print namenum.ljust(25) + '\t\t' + str(acctAllstar[i])
	print '---------- 11. Uruguay ----------'
	for i in range(countUruguay) :
		namenum = '%s (%d)' %(nameUruguay[i], numUruguay[i])
		print namenum.ljust(25) + '\t\t' + str(acctUruguay[i])
	print '---------- 12. Belgium ----------'
	for i in range(countBelgium) :
		namenum = '%s (%d)' %(nameBelgium[i], numBelgium[i])
		print namenum.ljust(25) + '\t\t' + str(acctBelgium[i])
	print '---------- 13. Croatia ----------'
	for i in range(countCroatia) :
		namenum = '%s (%d)' %(nameCroatia[i], numCroatia[i])
		print namenum.ljust(25) + '\t\t' + str(acctCroatia[i])
	print '---------- 14. Chile ----------'
	for i in range(countChile) :
		namenum = '%s (%d)' %(nameChile[i], numChile[i])
		print namenum.ljust(25) + '\t\t' + str(acctChile[i])
	print '---------- 15. Japan ----------'
	for i in range(countJapan) :
		namenum = '%s (%d)' %(nameJapan[i], numJapan[i])
		print namenum.ljust(25) + '\t\t' + str(acctJapan[i])
	print '---------- 16. Korea ----------'
	for i in range(countKorea) :
		namenum = '%s (%d)' %(nameKorea[i], numKorea[i])
		print namenum.ljust(25) + '\t\t' + str(acctKorea[i])
