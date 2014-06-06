#!/usr/bin/python
#encoding=utf-8

from keymap import login, logout, sure, down, clickNum, up, view, blank
from keymap import key, cap, ctl, sht, tab, ent 

# key delay
kDelay = 30
# tab delay
tDelay = 100
# login or logout delay
lDelay = 2000
# enter delay
eDelay = 1500
# sure delay
sDelay = 1500
# view delay
vDelay = 3000
# copy delay
cDelay = 1000

accountfile = r'./accounts.txt'
accountfile = open(accountfile, 'r')
password = accountfile.readline().strip('\n')
accountCtx = accountfile.readlines()
accountfile.close()
# remove '\n' in each account string
accounts = []
for i in range(len(accountCtx)) :
	accounts.append(accountCtx[i].strip('\n'))

# script file
scriptfile = './scripts/script_view.txt'
scriptfile = open(scriptfile, 'w+')
scriptfile.write('循环：1\r\n')
for account in accounts :
	scriptfile.write('延时：' + str(lDelay) + '\r\n')
	scriptfile.write('坐标：' + login + '\r\n')
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(lDelay) + '\r\n')
	scriptfile.write('坐标：' + tab + '\r\n')
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(tDelay) + '\r\n')
	# input account
	for char in account :		
		scriptfile.write('坐标：' + key[char] + '\r\n')
		scriptfile.write('鼠标：左键\r\n')
		scriptfile.write('延时：' + str(kDelay) + '\r\n')
	scriptfile.write('坐标：' + sht + '\r\n')
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(kDelay) + '\r\n')
	scriptfile.write('坐标：' + key['2'] + '\r\n')
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(kDelay) + '\r\n')
	scriptfile.write('坐标：' + key['1'] + '\r\n') 
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(kDelay) + '\r\n')
	scriptfile.write('坐标：' + key['6'] + '\r\n') 
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(kDelay) + '\r\n')
	scriptfile.write('坐标：' + key['3'] + '\r\n') 
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(kDelay) + '\r\n')
	scriptfile.write('坐标：' + key['.'] + '\r\n') 
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(kDelay) + '\r\n')
	scriptfile.write('坐标：' + key['c'] + '\r\n') 
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(kDelay) + '\r\n')
	scriptfile.write('坐标：' + key['o'] + '\r\n') 
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(kDelay) + '\r\n')
	scriptfile.write('坐标：' + key['m'] + '\r\n') 
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(kDelay) + '\r\n')
	scriptfile.write('坐标：' + tab + '\r\n')
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(tDelay) + '\r\n')
	# input password
	for char in password :
		scriptfile.write('坐标：' + key[char] + '\r\n')
		scriptfile.write('鼠标：左键\r\n')
		scriptfile.write('延时：' + str(kDelay) + '\r\n')
	scriptfile.write('坐标：' + tab + '\r\n')
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(tDelay) + '\r\n')
	# click enter
	scriptfile.write('坐标：' + ent + '\r\n')
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(eDelay) + '\r\n')
	# click sure
	scriptfile.write('坐标：' + sure + '\r\n')
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(sDelay) + '\r\n')
	# page down 
	scriptfile.write('坐标：' + down + '\r\n')
	for i in range(clickNum) :
		scriptfile.write('鼠标：左键\r\n')
		scriptfile.write('延时：' + str(kDelay) + '\r\n')
	# click view
	scriptfile.write('延时：' + str(vDelay) + '\r\n')
	scriptfile.write('坐标：' + view + '\r\n')
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(vDelay) + '\r\n')
	# page up
	scriptfile.write('坐标：' + up + '\r\n')
	for i in range(clickNum) :
		scriptfile.write('鼠标：左键\r\n')
		scriptfile.write('延时：' + str(kDelay) + '\r\n')
	# click blank
	scriptfile.write('坐标：' + blank + '\r\n')
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(5 * kDelay) + '\r\n')
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(5 * kDelay) + '\r\n')
	# input Ctrl + A
	scriptfile.write('坐标：' + ctl + '\r\n')
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(kDelay) + '\r\n')
	scriptfile.write('坐标：' + key['a'] + '\r\n')
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(cDelay) + '\r\n')
	# input Ctrl + C
	scriptfile.write('坐标：' + ctl + '\r\n')
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(kDelay) + '\r\n')
	scriptfile.write('坐标：' + key['c'] + '\r\n')
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(cDelay) + '\r\n')
	# logout
	scriptfile.write('坐标：' + logout + '\r\n')
	scriptfile.write('鼠标：左键\r\n')
	scriptfile.write('延时：' + str(lDelay) + '\r\n')
scriptfile.close()
