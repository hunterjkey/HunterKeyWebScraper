#My Webscraper File
#

import time 
import urllib2
from lxml import html
import requests
#This next import doesn't have any real purpose in this code, it's just there from when I tried Splinter and since I left the code in this program, I should also include the import
from splinter import Browser
import pandas as pd
from bs4 import BeautifulSoup

print " "
print "-------------------------------------------------------------------------------"
print "X    X  XXXXXX  XXXXX    XXXXXX  XXXXXX  XXXXX    XXXX   XXXXX   XXXXXX  XXXXX"
print "X    X  X       X    X   X       X       X   XX  X    X  X    X  X       X   XX"
print "X XX X  XXXXXX  XXXXX    XXXXXX  X       XXXXX   XXXXXX  XXXXX   XXXXXX  XXXXX"
print "XX  XX  X       X    X        X  X       X  XX   X    X  X       X       X  XX"
print "X    X  XXXXXX  XXXXX    XXXXXX  XXXXXX  X   XX  X    X  X       XXXXXX  X   XX"
print "-------------------------------------------------------------------------------"

print " "
print "By: Hunter Key, Period 4"
print " "

#print "Unless you have Splinter and Pandas downloaded, this program won't function" 
#print "correctly. Use 'pip install pandas' and 'pip install splinter' to download them" 
#print "(ideally in a virtual environment). You can also access more information at" 
#print "'https://hackernoon.com/mastering-python-web-scraping-get-your-data-back-e9a5cc653d88'"

print " "
print "this program analyzes the changes to a website's __ during a period of seconds" 
print "you define. It does this 10 times, and then after that you will have to restart" 
print "the program."
print " "
global cnt

cnt = 0
#this variable determinew whether to use "Beaut()" depending on the site
yes = 0
#This next line is to ensure that my program doesn't shut down the first time it runs through the webpage
global prevdatastr
prevdatastr = "0"
lnk = raw_input("What is the url of the site you want to monitor?")
tm = int(raw_input("How many seconds do you want me to wait until I remonitor your site"))
print " "



def characCount():
	global prevdatastr
	
	# open a connection to the URL
	webUrl = urllib2.urlopen(lnk)
  
  # get the result code and print it, this isn't applicable in a Scraper but might as well kep it for refernxe
	#print str(webUrl.getcode())
  
  # read the data from the URL and print it
	data = webUrl.read()
	datastr = str(data)
	
	if (cnt == 0):
		print "Finding base site to moniter"
	
	print "there are",len(datastr),"characters in the HTML code of this current webpage"
	if (cnt >= 1):
	#this if statement checks to see if this isn't the first time we open the webpage
	
		if prevdatastr == len(datastr):
			print "The website hasn't changed since you last checked it"
		else:
			print "The website has changed in some manner"
	
	prevdatastr = len(datastr)
	
def Splinter():
	# open a browser
	
	browser = Browser('chrome')

	# Width, Height
	browser.driver.set_window_size(640, 480)
	
	browser.visit(lnk)

	search_results_xpath = '//h3[@class="r"]/a'
	search_results = browser.find_by_xpath(search_results_xpath)  # returns list of link elements

	# iterate through list of link elements
	scraped_data = []
	for search_result in search_results:

		title = search_result.text.encode('utf8')  # trust me, clean data
		link = search_result["href"]
		scraped_data.append((title, link))

	# put all the data into a pandas dataframe
	df = pd.DataFrame(data=scraped_data, columns=["title", "link"])
	df.to_csv("links.csv")	# export to csv
	
def Beaut():
	global yes
	#query the website and return the html to the variable page
	page = urllib2.urlopen(lnk)
	
	# parse the html using beautiful soap and store in variable `soup`
	soup = BeautifulSoup(page, "html.parser")
	
	# Take out the <div> of name and get its value
	name_box = soup.find("span", attrs={"class": "instancename"})
	print name_box

	
	name = name_box.text.strip() # strip() is used to remove starting and trailing
	print name

	"""
	if (yes == 0):
		if (name_box == 13):
			if (12==11):
				name = name_box.text.strip() 
				# strip() is used to remove starting and trailing
				print name
		else:
			yes = 1
	"""

def lxml():
	"""
	page = requests.get(str(lnk))
	tree = html.fromstring(page.content)
	htmlElem = html.document_fromstring(sourceCode)
	
	
	#This will create a list of buyers:
	div = tree.xpath('//span[@id="yui_3_17_2_1_1511033227506_38"]/text()')

	print div
	"""
	headers= {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36"}
	page = requests.get(lnk
                    , headers=headers)
	tree = html.fromstring(page.content)
	assignment_name = tree.xpath('//a[@class="ac-algo fz-l ac-21th lh-24"]/text()')

	print(assignment_name)
	
while(cnt < 4):
	characCount()
	cnt += 1
	print " "
	time.sleep(tm)
	
print "Thank you for using WebScraper!"
