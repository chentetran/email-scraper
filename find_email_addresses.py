'''
Script for scraping all discoverable websites on a domain for email addresses
Usage: python find_email_addresses.py <domain>

Created by Vincent Tran, 10/7/2016
'''

import sys
import re
from collections import deque
from bs4 		 import BeautifulSoup

if len(sys.argv) == 1:
	print "Usage: python find_email_addresses.py <domain>"
	exit()

regex = re.compile(r"[\w\.-]+@[\w\.-]+")

domain = sys.argv[1]					# Get domain from command line
if 'http' not in domain:				# Add protocol to string if not found
	domain = 'https://' + domain

urlQueue = deque()						# Queue to track urls to visit
urlsVisited = []						# List to track urls already visited
urlQueue.append(domain)

while len(urlQueue):
	# 1. Grab emails from first 
	# 2. Grab any urls (should check that its on the domain)
	# 3. Add urls to queue


