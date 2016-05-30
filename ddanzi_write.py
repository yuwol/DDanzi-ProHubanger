#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 
# Login Module
# 
# Author: 0xb0a1
# Since: 28 May 2016
# Target: http://www.ddanzi.com/index.php?mid=free
# Tested on: Python 2.7.10 (OSX 10.11.5)
# Required
# 	requests ( # easy_install requests )

from datetime import datetime
import requests

def write_article(s, html, title):
	URL = 'http://www.ddanzi.com/index.php?mid=free&act=dispBoardWrite'	
	write_payload = {
		'_filter' : 'insert',	
		'error_return_url' : 'http://www.ddanzi.com/index.php?act=dispMemberInfo',
		'act' : 'procBoardInsertDocument',
		'mid' : 'free',
		'is_adult' : 'Y',
		'title' : title,
		'content' : html
	}

	# Write Article
	print('[DDanzi ProHubanger][%s] Writing Article... ' % (str(datetime.today())))
	r = s.post(URL, write_payload)

	# Temporary Check
	if r.status_code == 200:
		print('[DDanzi ProHubanger][%s] Succeed! (status_code=%s)' % (str(datetime.today()), r.status_code))
		return True
	else:
		print('[DDanzi ProHubanger][%s] Failed! (status_code=%s)' % (str(datetime.today()), r.status_code))
		return False