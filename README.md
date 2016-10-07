# email-scraper
Python script; takes a domain name and prints out any emails found on the domain

## Libraries used:
 - mechanize

## Running list of things that need fixing:
 - Simple appends 'http://' to domains if 'http' not found in string -- make more elegant!
 - Handle errors from mechanize like... 'request disallowed by robots.txt', etc.
 - How to handle http vs https?
    - If no protocol is specified and the script assumes http, but the website redirects http->https, source code from the website won't be correct
 -

## Got help from
 - http://stackoverflow.com/questions/17681670/extract-email-sub-strings-from-large-document



