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

def login(id, pwd):
	LOGIN_URL = 'https://www.ddanzi.com/index.php?act=dispMemberLoginForm'

	login_payload = {
		'success_return_url': 'http://www.ddanzi.com/index.php?act=dispMemberInfo',
		'act': 'procMemberLogin',
		'user_id': id,
		'password': pwd,
		'keep_signed': 'Y'
	}

	print('[DDanzi ProHubanger][%s] Logging in...' % str(datetime.today()))
	s = requests.session()
	r = s.post(LOGIN_URL, login_payload)

	if r.content.find('아이디 또는 비밀번호가 잘못 되었습니다.') >= 0:
		print('[DDanzi ProHubanger][%s] Login Failed! (아이디 또는 비밀번호가 잘못 되었습니다.)' % str(datetime.today()))
		return None
	elif r.status_code != 200:
		print('[DDanzi ProHubanger][%s] Login Failed! (status_code=%s)' % str(datetime.today()), r.status_code)
	else:
		print('[DDanzi ProHubanger][%s] Logged in! (id=%s, status_code=%s)' % (str(datetime.today()), id, r.status_code))
		return s
