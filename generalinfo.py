# Kyle Drummond
# Senior Seminar Capstone Project

# for the wikipedia page
# compile with python3 instead of python

import requests
import csv
from datetime import datetime
from bs4 import BeautifulSoup

# download the page
myurl = requests.get("https://en.wikipedia.org/wiki/Goodyear_Tire_and_Rubber_Company")
# create BeautifulSoup object
soup = BeautifulSoup(myurl.text, 'html.parser')

# pull the class containing all tire name
name = soup.find(class_ = 'logo')
# pull the div in the class
nameinfo = name.find('div')

# just grab text inbetween the div
nametext = nameinfo.text

# print information about goodyear logo on wiki page
#print(nameinfo)

# now, print type of company, private or public
#status  = soup.find(class_ = 'category')
#for link in soup.select('td.category a'):
    #print link.text

# now get the ceo information
#for employee in soup.select('td.agent a'):
#    print employee.text

# print area served
#area = soup.find(class_ = 'infobox vcard')
#print(area)


# grab information in bold on the left hand side
vcard = soup.find(class_ = 'infobox vcard')
rows = vcard.find_all('tr')
first = []
for row in rows:
    cols = row.find_all('th')
    for x in cols:
      first.append(str(x.text.strip()))           ## Storing data in string form
    #first.append([x.text.strip() for x in cols])        ## Storing data in list form 
    #print cols

vcard = soup.find(class_ = 'infobox vcard')
rows = vcard.find_all('tr')
second = []
flag = 0
for row in rows:
    cols2 = row.find_all('td')
    for x in cols2:
      if (flag == 0):      ## First time flag is 0 so skip this
        flag = 1           ## Initialize flag = 1 to skip this condition from next time
      else:                ## In else part do your what you are doing
        second.append(str(x.text.strip()))        ## Storing data in string form
    #second.append([x.text.strip() for x in cols2])      ## Storing data in list form 
    #print second


with open('companyInfo.csv', 'w') as csv_file:
    for f,s in zip(first,second):
      wr = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL) ## Delimiter will automatically seperate it with ',' and quoting part will take whole part as one and not seperate it with ','
      wr.writerow([f,s])   ## writing row from list in list for, no need to add ',' in between
      print(f,s)

