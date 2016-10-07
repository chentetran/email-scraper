'''
Script for scraping all discoverable websites on a domain for email addresses
Usage: python find_email_addresses.py <domain>
'''

import sys
import mechanize
import re

if len(sys.argv) == 1:
	print "Usage: python find_email_addresses.py <domain>"
	exit()

regex = re.compile(r"[\w\.-]+@[\w\.-]+")

domain = sys.argv[1]					# Get domain from command line
if 'http' not in domain:				# Add protocol to string if not found
	domain = 'https://' + domain

browser = mechanize.Browser()
page = browser.open(domain)
source_code = page.read()

emails = list(set(re.findall(regex, source_code))) # Remove duplicates using set
print emails



