#------------------------------------------------------------------------------
# Name:        URL File Scraper
# Description: Educational
#
# Author:      Robert S. Spencer
#
# Created:     5/7/2016
# Python:      3.5
#------------------------------------------------------------------------------


import urllib as urllib
from bs4 import BeautifulSoup as bs
import os
import time

date = time.strftime("_%m.%d.%Y_%I.%M")
directory = 'Downloads' + date
os.makedirs(directory)

url = input("URL: ")

soup = bs(urllib.request.urlopen(url), "lxml")

for link in soup.findAll('a'):
    l = str(link.get('href'))
    print (l)

ext = input("Extension: ")

print ("Directory: ", directory, "\nFiles:")

for link in soup.findAll('a'):
    l = str(link.get('href'))

    if l[len(l)-len(ext):] == ext:

        for i in range(1,len(l)):
            if l[len(l)-1-i] == '/':
                n = i
                break
        print (" ", l[len(l)-n:])

        urllib.request.urlretrieve(l, filename = directory + '/' + l[len(l)-n:])

