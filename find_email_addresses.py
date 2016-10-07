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

# Regex taken from http://code.activestate.com/recipes/138889-extract-email-addresses-from-files/
regex = re.compile(r"[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}", re.IGNORECASE)

domain = sys.argv[1]					# Get domain from command line

if 'http' not in domain:				# Add protocol to string if not found
	domain = 'https://' + domain

urlQueue 	= deque()					# Queue to track urls to visit
urlsVisited = set()						# Set to track urls already visited
emails 		= set()
urlQueue.append(domain)
browser 	= mechanize.Browser()

while len(urlQueue):
	url = urlQueue.popleft()
	if url in urlsVisited:				# Already visited, skip
		continue

	# 0. Get source code & parse
	try:
		page 		= browser.open(url)
		source_code = page.read()
		parsed_source = BeautifulSoup(source_code, "html.parser")

		# 1. Grab emails from page @ front of queue 
		emails.update(re.findall(regex, parsed_source.get_text()))

		# 2. Grab any urls & append to queue
		# Find links by searching for <href> inside of <a>
		for a in parsed_source.find_all('a'):
			link = a.get('href')

			if 'http' not in link:		# Account for relative links
				link = domain + link
			elif domain in link:		# Only accept links within given domain
				urlQueue.append(link)
	except:
		pass

	urlsVisited.add(url)

if len(emails) == 0:
	print "[-] No emails found"
else:
	print "[+] Found the following emails:"
	for email in list(emails):
		print "[+] " + email

