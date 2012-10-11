#This code is written to scrape book info off of amazon. Please use for small applicatiosn as this will cause a samll amount of toll on their pages. However, in a larg application, this is the equivilant of DDOS
#CopyRight Joubin Jabbari
from bs4 import BeautifulSoup
from stripogram import html2text
import commands
import os
import urllib2
import sys
import re
import string
import array
response = urllib2.urlopen(sys.argv[1])
html = response.read()
soup = BeautifulSoup(html)
outter = soup.find("div",{"id":"ps-content", "class":"bucket"})
final = outter.find("div", {"class":"buying"})
asd = str(final)
text = os.popen("echo '"  +asd + "' | html2text " ).read()
array = text.split("|")
db = []
for i in range(len(array)):
	temp = array[i].split(":")
	db.append(temp[1])
db = [x.strip('\n') for x in db]
db = [x.strip(' ') for x in db]



# The code above here lodas date, isbn(S) and edition

#The part below get the books name


outter = soup.find("h1",{"class":"parseasinTitle"})
asd = str(outter)


s = BeautifulSoup(asd)
bookname = s.get_text()
db.append(bookname)
print db
