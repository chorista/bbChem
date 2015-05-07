import urllib, urllib2, cookielib
import base64
import getpass
from selenium import webdriver
from bs4 import BeautifulSoup


#id
username =input('ID: ')

#password
password=getpass.getpass()
#base64 encoding
encoded_pw=base64.encodestring(password)
encoded_pw=encoded_pw[:-1]

cj=cookielib.CookieJar()
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Testing')]
urllib2. install_opener(opener)

url="http://bb.unist.ac.kr/webapps/login/?action=login"

payload={'user_id':username, 'encoded_pw':encoded_pw}
data=urllib.urlencode(payload)
req=urllib2.Request(url, data)
resp=urllib2.urlopen(req)

link = raw_input("Copy your test link: ")
req=urllib2.Request(link)
resp=urllib2.urlopen(req)



f = open( "chemistry.txt", 'a') 
f.write(resp.read())
f.close()
