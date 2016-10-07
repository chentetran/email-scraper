'''
Script for scraping all discoverable websites on a domain for email addresses
Usage: python find_email_addresses.py <domain>
'''

import sys
import mechanize

# Get domain from command line
if len(sys.argv) == 1:
	print "Usage: python find_email_addresses.py <domain>"
	exit()

domain = sys.argv[1]
if 'http' not in domain:
	domain = 'http://' + domain
print domain

browser = mechanize.Browser()


page = browser.open(domain)
source_code = page.read()
print source_code




