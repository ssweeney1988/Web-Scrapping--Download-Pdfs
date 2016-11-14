#import urlpage
import urllib2
import os
import sys
import requests, webbrowser

from bs4 import BeautifulSoup

url= "http://security.cs.rpi.edu/courses/binexp-spring2015/"
download_path= "C:\Python\mose"


res = requests.get(url)
res.raise_for_status()  # Raises if there is an error
soup= BeautifulSoup(res.text, "html.parser")


#print len(res.text) 

i=0

for tag in soup.findAll('a', href=True): # find <a> tags with href in it so you know its for urls
	#tag['href'] = urlparse.urljoin(url, tag['href']) 
	#this is so if it doesnt contain the full url is it adding the url to it
	#print tag
	 if os.path.splitext(os.path.basename(tag['href']))[1] == '.pdf':
		#print tag
		#print os.path.basename(tag['href']
		print tag['href']
		print tag		
		
		print "\n[*] Downloading: %s" %(os.path.basename(tag['href']))

		f = open(download_path + "\\" + os.path.basename(tag['href']))
		#open('C:\Python\mose\RomeoAndJuliet.txt', 'wb')

		print f
		f.write(current.read())
		f.close()
		i+=1
print tag
print "\n[*] Downloaded %d files" %(i+1)