'''
Script for scraping all discoverable websites on a domain for email addresses
Usage: python find_email_addresses.py <domain>

Created by Vincent Tran, 10/7/2016
'''

import sys
import re
from bs4 import BeautifulSoup

if len(sys.argv) == 1:
	print "Usage: python find_email_addresses.py <domain>"
	exit()

regex = re.compile(r"[\w\.-]+@[\w\.-]+")

domain = sys.argv[1]					# Get domain from command line
if 'http' not in domain:				# Add protocol to string if not found
	domain = 'https://' + domain



# emails = list(set(re.findall(regex, source_code))) # Remove duplicates using set

# if not emails:
# 	print "[-] No emails found"
# else:
# 	print "[+] Found these email addresses:"
# 	for email in emails:
# 		print email
