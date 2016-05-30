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
# 	BeautifulSoup (https://www.crummy.com/software/BeautifulSoup/)

from bs4 import BeautifulSoup
from datetime import datetime
from datetime import timedelta
import requests
import logging

# s: Session
# sp_num: Start page number
# ep_num: End page numbe
# p_hour: Past hour
def crawl(s, sp_num, ep_num, p_hour):
	ex_list = []
	lastest_date = ""
	ended_page = sp_num
	dt = datetime.today()
	article_time = dt
	st_date = dt
	article_start_time = "%04d.%02d.%02d %02d:%02d:%02d" % (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
	article_end_time = dt-timedelta(hours=p_hour)
	global_date = "%04d-%02d-%02d %02d:%02d:%02d" % (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
	today = "%04d.%02d.%02d" % (dt.year, dt.month, dt.day)
	fmt_date_dot = "%Y.%m.%d %H:%M:%S.%f"
	fmt_date_dash = "%Y-%m-%d %H:%M:%S.%f"

	print "[DDanzi ProHubanger][%s] Starting Crawling %s to %s (-%d hours)" % \
	(str(datetime.today()), article_time, article_end_time, p_hour)

	for i in range(sp_num, ep_num):
		print "[DDanzi ProHubanger][%s]   Opening Page: %d ([%s] accumulated count: %d)" % ( str(datetime.today()), i, lastest_date, len(ex_list))
		r = s.get("http://www.ddanzi.com/index.php?mid=free&page=%d" % (i) )		
		soup = BeautifulSoup(r.content, "html.parser")		
		
		# article tr tag
		for a in soup.find_all("tr"):
			ex = a.find("i", class_="fa fa-exclamation-triangle")			
			if ex:
				u = a.find("img")			
				f_no = a.find("td", class_="no")			
				f_title = a.find("td", class_="title")
				if u == None:
					u = ""
				f_author = a.find("td", class_="author")	
				f_time = a.find("td", class_="time")	
				f_readnum = a.find("td", class_="readNum")	
				f_votenum = a.find("td", class_="voteNum")	

				lastest_date = f_time.get_text()
				
				# d+day calculation
				# f_time.get_text()
				# 	fmt_date_dot = "%Y.%m.%d %H:%M:%S.%f"
				# 	fmt_date_dash = "%Y-%m-%d %H:%M:%S.%f"			
				
				if len(f_time.get_text()) != 8:    # date : yyyy.mm.dd
					article_time = datetime.strptime(f_time.get_text() + " 0:0:0.00000", fmt_date_dot)			
				else:								# time : hh:mm:ss
					article_time = datetime.strptime(today + " " + f_time.get_text() + ".00000", fmt_date_dot)
					

				# list			
				ex_list.append(
					[f_no.get_text(), f_title.a.get('href'), 
					f_title.a.get_text(), u, f_author.a.get_text(), 
					f_time.get_text(), f_readnum.get_text(), f_votenum.get_text()]
					)

		# dday exit condition
		if article_time < article_end_time:
			print("[DDanzi ProHubanger][%s] Exit Condition: %s " % (str(datetime.today()), str(st_date - article_time)))
			break

		ended_page += 1

	# Ellipsed Time
	dt = datetime.today()
	search_end_time = "%04d.%02d.%02d %02d:%02d:%02d" % (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
	search_ellipsed_time = datetime.strptime(search_end_time, "%Y.%m.%d %H:%M:%S") - datetime.strptime(article_start_time, "%Y.%m.%d %H:%M:%S")


	# Crawling Info
	crawl_info = {}
	crawl_info['global_time'] = global_date
	crawl_info['processed_time'] = str(search_ellipsed_time.seconds)
	crawl_info['total_articles'] = str(len(ex_list))
	crawl_info['page_searched'] = str(sp_num) + " - " + str(ended_page)
	crawl_info['result_from'] = str(p_hour)

	#print(crawl_info)

	return ex_list, crawl_info


