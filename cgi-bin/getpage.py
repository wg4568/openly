#! /usr/bin/python

#Import stuff
import httplib
from time import strftime
import cgi
import os 
import urllib2

#Print header
print "Content-Type: text/html"

#Get form values
form     = cgi.FieldStorage()
website  = form.getvalue("url")
userip = os.environ["REMOTE_ADDR"]

#Check for http as start of URL
if website[:4] != "http":
	website = "http://" + website

#Write to the log file
f= open("../../../logs/openly.txt", "a")
f.write(strftime('%D - %H:%M:%S') + "|" + userip + "|" + website + "\n")
f.close()

#Download requested website
page= urllib2.urlopen(website)

#Print the websites HTML
print '''
%s
''' % page.read()
