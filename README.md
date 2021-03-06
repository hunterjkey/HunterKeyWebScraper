# Hunter Key's Website Scraper
This Program takes the HTML code from a website that you gives it and checks for changes in the number of characters within the whole HTML 
code, and for changes within the first paragraph tag of that website. This program is multiuse and can scrape a larger number/range of sites. As long as the website is secure (i.e. "https://"), the program can scrape it.

I pulled code from https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe, the Twilio tutorial at https://jamesbvaughan.com/python-twilio-scraping/, and Walker's Datetime and Webdata snippets into my final product. 

# What Each File in this Repository is:
Final Versions: 
>> Contains two versions of my program (each of them is slightly different), it includes the version given below in a seperate file.
                        
Attempt Documentation: 
>> Contains other kinds of web scrapers that I attempted using but was unsuccessful. It's more of a record if I want to try to fix some of them in the future.
                        
Program Flow Charts: 
>> The XML and png file containing my flow chart.
                        
ReadMe: 
>> My ReadMe file that displays all of this

Version 3:
>> The Python Code for my Web Scraper, install instructions are given below this.

# Instructions:

1) You NEED to have Python 2.7.14 downloaded on your computer.
2) Unless you already have a virtual environment you want to use, create a folder on your desktop and create a virtual envirenment within it. This can be done by using the following commands (credit to Liam Dunbar):
 ```
  cd C:\Python27\Scripts                                         
  pip install virtualenv                                         
  cd C:\Users\"Username"\Documents\                              
  mkdir HunterScraper                                            
  cd HunterScraper                                               
  C:\Python27\Scripts\virtualenv.exe -p C:\Python27\python.exe   
  .lpvenv\Scripts\activate                                       
 ```
3) Paste Version 3 (It's stored within the folder "Final Versions," it's the second one there. DON'T USE VERSION ONE. It can also be found in "Version 3," the last file in the repository) into a Notepad++ document and save it into the folder that has your virtual environment under a name of your choice ("HunterWebScraper.py" is a good choice). ANYWHERE ELSE AND IT WON'T WORK.
4) Open the virtual envirenment that houses "Version 2" in the command line. This can be done by typing/pasting ".lpvenv\Scripts\activate" into the command line while inside the folder containing the virtual environment. 
5) After that, type/paste:
```
  pip install BeautifulSoup4
```
into the command line. This downloads BeautfulSoup, a python library that is essential to the functionality of this program. You will also need to type/paste:
```
  pip install Twilio
```
Into the command line, this allows you to use Twilio, a online service that will allow you to recieve text updates on your phone. Wait for these both to download before continuing.

6) Type "python HunterWebScraper.py" (or whatever you named my file on your computer) into the command line (Do not include any other parameters, this will only lead to an error) and press enter.
7) A screen will appear detailing my Web Scraper and how it works. A input will appear at the bottom asking for a link, ensure that the link that you enter starts with an "https://" because otherwise, you will encounter an error along the lines of "HTML forbidden" (and simply adding it to the front of the link won't solve the problem, it needs to be a part of the original link you copied). Enter the link and press enter.
8) There are two more inputs after this, one for the number of times the program runs and one for the time it waits between scaping, enter a value for each of these.
9) If all the previous steps were followed correctly, the Scraper will begin running and scrape the website per your parameters.


# Core Algorithm Flowchart
![flowchart](https://github.com/hunterjkey/HunterKeyWebScraper/blob/master/Program%20Flow%20Chart.png?raw=true)

(credit to Seth on the command to display this png)
