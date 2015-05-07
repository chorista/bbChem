from BeautifulSoup import BeautifulSoup
import urllib2

url = "http://bb.unist.ac.kr"
handle = urllib2.urlopen(url)
data= handle.read()
soup = BeautifulSoup(data)
article=str(soup('div', {'class':'legal',}))
print article.decode('utf8')
