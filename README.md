# email-scraper
Python script; takes a domain name and prints out any emails found on the domain

## To run:
 1. Make sure you have python and pip installed on your computer. If you don't, check out https://www.python.org/downloads/.
 2. Install the mechanize library so it can be used in this program. `pip install mechanize`. You might have to run as superuser.
 3. Clone this repo.
 4. Inside the cloned repo, run `python find_email_addresses.py <domain>`, where <domain> is a url, like 'google.com'. It's even better if you include the protocol, ie 'https://google.com'.
 5. Profit


## Libraries used:
 - mechanize

## Running list of things that need fixing:
 - Simple appends 'http://' to domains if 'http' not found in string -- make more elegant!
 - Handle errors from mechanize like... 'request disallowed by robots.txt', etc.
 - How to handle http vs https? If no protocol is specified and the script assumes http, but the website redirects http->https, source code from the website won't be correct
 -

## Got help from
 - http://stackoverflow.com/questions/17681670/extract-email-sub-strings-from-large-document



