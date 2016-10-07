'''
Script for scraping all discoverable websites on a domain for email addresses
Usage: python find_email_addresses.py <domain>

Created by Vincent Tran, 10/7/2016
'''

import sys
import re
import mechanize
from collections import deque
from bs4 		 import BeautifulSoup

if len(sys.argv) == 1:
	print "Usage: python find_email_addresses.py <domain>"
	exit()

regex = re.compile(r"[\w\.-]+@[\w\.-]+")

domain = sys.argv[1]					# Get domain from command line
if 'http' not in domain:				# Add protocol to string if not found
	domain = 'https://' + domain

urlQueue 	= deque()					# Queue to track urls to visit
urlsVisited = set()						# Set to track urls already visited
emails 		= set()
urlQueue.append(domain)

while len(urlQueue):
	# 0. Get source code & parse
	browser = mechanize.Browser()
	page = browser.open(domain)
	source_code = page.read()
	source_text = BeautifulSoup(source_code, "html.parser").get_text()

	# 1. Grab emails from page @ front of queue 
	emails.update(re.findall(regex, source_text))

	# 2. Grab any urls (TODO: should check that its on the domain)
	urlQueue.extend()

	# 3. Add urls to queue

for email in list(emails):
	print email

