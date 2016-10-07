# email-scraper
Python script; takes a domain name and prints out any emails found on the domain

## To run:
 1. Make sure you have python and pip installed on your computer. If you don't, check out https://www.python.org/downloads/.
 2. Install the beautifulsoup and mechanize libraries so it can be used in this program. `pip install bs4` and `pip install mechanize`. You might have to run as superuser.
 3. Clone this repo.
 4. Inside the cloned repo, run `python find_email_addresses.py <domain>`, where <domain> is a url, like 'google.com'. It's even better if you include the protocol, ie 'https://google.com'.
 5. Profit

## Example use:
I've created a test website to show this email scraper's ability. You can check out the website at [chentetran.github.io/email-scraper]. Other popular websites may not work because of redirects or a robots.txt ban (errors because of these are silenced).


## Libraries used:
 - BeautifulSoup
 - mechanize

## Running list of things that need fixing or might not behave as expected:
 - Simply appends 'http://' to domains if 'http' not found in string -- should make more elegant!
 - How to handle http vs https? If no protocol is specified and the script assumes http, but the website redirects http->https, source code from the website won't be correct
 - In current implementation, `hello.com/page` and `hello.com//page` and `hello.com/./page` are treated as different links, so they may be visited more than once. Perhaps there's a library for URL cleaner-uppers?
 - If you give a specific page (not a homepage) it will not traverse into other pages that aren't children of that page.
   Example: If you enter `hello.com/`, it will visit every page that is `hello.com/*`.
   If you enter `hello.com/world`, it will only visit pages that are `hello.com/world/*`.



