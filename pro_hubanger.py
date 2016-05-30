#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 
# Pro Hubanger
# 
# Author: 0xb0a1
# Since: 28 May 2016
# Target: http://www.ddanzi.com/index.php?mid=free
# Tested on: Python 2.7.10 (OSX 10.11.5)
# Required
# 	requests ( # easy_install requests )

from ddanzi_login import login
from ddanzi_write import write_article
from ddanzi_crawl import crawl
from ddanzi_output import fileout
from ddanzi_output import htmlout
import requests
import sys

# Parameters
p_id = ''
p_pwd = ''
n_st_page = 1
n_en_page = 1000
n_p_hour = 3

if len(sys.argv) != 6:
	print('check arguments (%d)' % len(sys.argv))
	sys.exit(1)
else:
	p_id = sys.argv[1]
	p_pwd = sys.argv[2]
	n_st_page = int(sys.argv[3])
	n_en_page = int(sys.argv[4])
	n_p_hour = int(sys.argv[5])

# Login
s = login(p_id, p_pwd)
if s == None:
	sys.exit(1)

# Crawl
ex_list, info = crawl(s, n_st_page, n_en_page, n_p_hour)
if len(ex_list) < 1:
	sys.exit(1)

# Output
#fileout(ex_list, info, info['global_time'])
h = htmlout(ex_list, info)
if len(h) < 1:
	sys.exit(1)

# Write Article
if write_article(s, h, '[프로후방er] 현 시간부 후방모음 (-%dH)' % n_p_hour):
	sys.exit(0)
else:	
	sys.exit(1)

# Abnormal Exit
sys.exit(1)
