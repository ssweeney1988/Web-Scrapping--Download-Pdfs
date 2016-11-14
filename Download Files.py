#import urlpage
import urllib2
import os
import sys
import requests

from bs4 import BeautifulSoup

url= "http://www.nswrealestate.com.au/renting/tenancy-application"
download_path= "C:\Python\mose"


res = requests.get(url)
res.raise_for_status()  # Raises if there is an error
soup= BeautifulSoup(res.text, "html.parser")


i=0

for tag in soup.findAll('a', href=True): # find <a> tags with href in it so you know its for urls
	#tag['href'] = urlparse.urljoin(url, tag['href']) 
	#this is so if it doesnt contain the full url is it adding the url to it

	if os.path.splitext(os.path.basename(tag['href']))[1] == '.pdf':
		current= urllib2.urlopen(tag['href'])
		print "\n[*] Downloading: %s" %(os.path.basename(tag['href']))

		f = open(download_path + "\\" + os.path.basename(tag['href'], 'wb'))
		f.write(current.read())
		f.close()
		i+=1
print "\n[*] Downloaded %d files" %(i+1)