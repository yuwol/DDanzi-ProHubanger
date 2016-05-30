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

from datetime import datetime

def fileout(l, info, filename):
	f = open(filename + ".html", "w") 
	f.write("<!DOCTYPE HTML><html><head><title>%s</title></head><body>" % info['global_time'] + "\n\n");
	f.write("<table style='width: 100%;'>" + "\n\n")
	f.write("<tr><th style='background-color: #4CAF50; color: white; height: 25px;'>No</th><th style='background-color: #4CAF50; color: white; height: 25px;'>Subject</th><th style='background-color: #4CAF50; color: white; height: 25px;'>Nickname</th><th style='background-color: #4CAF50; color: white; height: 25px;'>Time</th><th style='background-color: #4CAF50; color: white; height: 25px;'>Read</th><th style='background-color: #4CAF50; color: white; height: 25px;'>Vote</th></tr>" + "\n\n")
	for e in l:	
		f.write("<tr>" + "\n")
		f.write("<td style='border-bottom: 1px solid #ddd; padding: 5px;'>" + "\n")
		f.write(e[0].encode('utf-8').strip())
		f.write("</td>" + "\n")
		f.write("<td style='border-bottom: 1px solid #ddd; padding: 5px;'>")
		f.write("<a href='" + e[1].encode('utf-8').strip() + "'>" + e[2].encode('utf-8').strip() + e[3].encode('utf-8').strip() + "</a>")
		f.write("</td>" + "\n")	
		f.write("<td style='border-bottom: 1px solid #ddd; padding: 5px;'>")
		f.write(e[4].encode('utf-8').strip())
		f.write("</td>" + "\n")
		f.write("<td style='border-bottom: 1px solid #ddd; padding: 5px;'>")
		f.write(e[5].encode('utf-8').strip())
		f.write("</td>" + "\n")
		f.write("<td style='border-bottom: 1px solid #ddd; padding: 5px;'>")
		f.write(e[6].encode('utf-8').strip())
		f.write("</td>" + "\n")
		f.write("<td style='border-bottom: 1px solid #ddd; padding: 5px;'>")
		f.write(e[7].encode('utf-8').strip())
		f.write("</td>" + "\n")
		f.write("</tr>" + "\n\n")
	f.write("</table>" + "\n")
	f.write("<p align='right'>Update Time: " + info['global_time'] + "</p>")
	f.write("<p align='right'>Processed Time: " + info['processed_time'] + " secs" + "</p>")
	f.write("<p align='right'>Total Articles: " + info['total_articles'] + "</p>")
	f.write("<p align='right'>Page Searched: " + info['page_searched'] + "</p>")
	f.write("<p align='right'>Results From: " + info['result_from'] + " hours ago." + "</p>\n\n\n")

	f.write("</body></html>" + "\n")
	f.close()

	print("[DDanzi ProHubanger][%s] %s.html Written." % (str(datetime.today()), filename))


def htmlout(l, info):
	html = ''
	html += "<table style='width: 100%;'>" + "\n\n"
	html += "<tr><th style='background-color: #4CAF50; color: white; height: 25px;'>No</th><th style='background-color: #4CAF50; color: white; height: 25px;'>Subject</th><th style='background-color: #4CAF50; color: white; height: 25px;'>Nickname</th><th style='background-color: #4CAF50; color: white; height: 25px;'>Time</th><th style='background-color: #4CAF50; color: white; height: 25px;'>Read</th><th style='background-color: #4CAF50; color: white; height: 25px;'>Vote</th></tr>" + "\n\n"
	for e in l:	
		html += "<tr>" + "\n"
		html += "<td style='border-bottom: 1px solid #ddd; padding: 5px;'>" + "\n"
		html += e[0].encode('utf-8').strip()
		html += "</td>" + "\n"
		html += "<td style='border-bottom: 1px solid #ddd; padding: 5px;'>"
		html += "<a href='" + e[1].encode('utf-8').strip() + "'>" + e[2].encode('utf-8').strip() + e[3].encode('utf-8').strip() + "</a>"
		html += "</td>" + "\n"
		html += "<td style='border-bottom: 1px solid #ddd; padding: 5px;'>"
		html += e[4].encode('utf-8').strip()
		html += "</td>" + "\n"
		html += "<td style='border-bottom: 1px solid #ddd; padding: 5px;'>"
		html += e[5].encode('utf-8').strip()
		html += "</td>" + "\n"
		html += "<td style='border-bottom: 1px solid #ddd; padding: 5px;'>"
		html += e[6].encode('utf-8').strip()
		html += "</td>" + "\n"
		html += "<td style='border-bottom: 1px solid #ddd; padding: 5px;'>"
		html += e[7].encode('utf-8').strip()
		html += "</td>" + "\n"
		html += "</tr>" + "\n\n"
	html += "</table>" + "\n"
	html += "<p align='right'>Update Time: " + info['global_time'] + "</p>"
	html += "<p align='right'>Processed Time: " + info['processed_time'] + " secs" + "</p>"
	html += "<p align='right'>Total Articles: " + info['total_articles'] + "</p>"
	html += "<p align='right'>Page Searched: " + info['page_searched'] + "</p>"
	html += "<p align='right'>Results From: " + info['result_from'] + " hours ago." + "</p>\n\n\n"

	return html


