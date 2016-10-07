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

''' 
Takes a string text to search for emails
Returns a list of all emails found
'''
def grabEmails(text):
	return re.findall(regex, text)

'''
Takes a BeautifulSoup object (parsed html) and a string url domain
Returns a list of links that are within the given domain
'''
def grabLinks(parsed_text, domain):
	links = []
	
	# Find links by searching for <href> inside of <a>
	for a in parsed_text.find_all('a'):
		link = a.get('href')

		if 'http' not in link:		# Account for relative links
			link = domain + link
		if domain in link:		# Only accept links within given domain
			links.append(link)

	return links

'''
Takes a string domain and a compiled regex
Returns a list of all emails found
'''
def scrapeEmails(domain, regex):
	urlQueue 	= deque()					# Queue to track urls to visit
	urlsVisited = set()						# Set to track urls already visited
	emails 		= set()
	urlQueue.append(domain)
	browser 	= mechanize.Browser()

	while len(urlQueue):
		url = urlQueue.popleft()
		if url in urlsVisited:				# Already visited, skip
			continue

		try:
			page 		= browser.open(url)
			source_code = page.read()
			parsed_source = BeautifulSoup(source_code, "html.parser")

			emails.update(grabEmails(parsed_source.get_text())) # Grab emails
			urlQueue.extend(grabLinks(parsed_source, domain))	# Grab urls and add to queue
		
		except:
			pass

		urlsVisited.add(url)

	return list(emails)

if __name__ == "__main__":
	if len(sys.argv) == 1:
		print "Usage: python find_email_addresses.py <domain>"
		exit()

	# Regex taken from 
	# http://code.activestate.com/recipes/138889-extract-email-addresses-from-files/
	regex = re.compile(r"[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}", re.IGNORECASE)

	domain = sys.argv[1]					# Get domain from command line

	if 'http' not in domain:				# Add protocol to string if not found
		domain = 'https://' + domain
	domain += '/'


	emails = scrapeEmails(domain, regex)

	if len(emails) == 0:
		print "[-] No emails found"
	else:
		print "[+] Found the following emails:"
		for email in emails:
			print "	" + email

