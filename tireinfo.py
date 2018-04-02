# Kyle Drummond
# Senior Seminar Capstone Project

# for tire and review page
# compile with just python

import requests
import csv
from datetime import datetime
from bs4 import BeautifulSoup


# download the page
myurl = requests.get("https://www.goodyearautoservice.com/en-US/tires/all-season")


# create BeautifulSoup object
page_soup = BeautifulSoup(myurl.text, 'html.parser')

'''
# get all the tire info we need, specify where the info is located
h3 = soup.find_all('h3', class_ = "baseball-card__title")

for tireblock in h3:
		# find the children in tire block
		children = tireblock.findChildren()
		first = []
		for child in children:
			# grab the text in the b tags
			print(child.get_text())

price = soup.find_all('span', class_ = "baseball-card__price")
for listprice in price:
	orig = price[0].text.strip()
	print(orig)
'''
containers = page_soup.findAll("div",{"class":"baseball-card baseball-card__wrapper"})

filename = "product.csv"
o = open(filename, "w")

header_row = "Tire, Price, Five Star Reviews\n"

o.write(header_row)

for container in containers:
	# product name
	tire_name = container.findAll("a", {"class":"link-chevron"})
	product_name = unicode(tire_name[0].text).encode('utf-8').strip()
	product_name = product_name.replace('\n','')
	print(product_name)

	# tire price
	price = container.findAll("span", {"class":"baseball-card__price"})
	list_price = unicode(price[0].text).encode('utf-8').strip()
	print(list_price)

	# tire review
	reviews = container.findAll("span", {"class": "my-store__rating__stars"})
	if reviews:
		tire_reviews = unicode(reviews[0].text).encode('utf-8').strip()
		print(tire_reviews)
	else:
		tire_reviews="No reviews available"

	print("Tire: " + product_name)
	print("Price: " + list_price)
	print("Five Star Reviews: " + tire_reviews)

	o.write(product_name + "," + list_price + "," + tire_reviews + "\n")

o.close()