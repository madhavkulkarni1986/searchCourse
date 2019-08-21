'''
Inspired by Medium post => Post: Build a Searchable Course Catalog => https://stories.mlh.io/build-a-searchable-course-catalog-8a0553824af5
				 Author	=> Irfaan Khalid(https://stories.mlh.io/@Irfdawg).

The original post shows the implementation using Node.js and some additional libraries. Here I am use Python; request and BeautifulSoup modules :-)
'''

import requests
from bs4 import BeautifulSoup as bs
import sys
import re

def search(searchterm):
	''' Define the URL to scrape '''
	URL='http://catalogs.rutgers.edu/generated/nb-ug_current/pg159.html'

	''' Use requests.get to fetch the web page'''
	page=requests.get(URL)
	if(page.status_code != 200):
		print("Web adress returned error. Error code: {}".format(page.status_code))
		sys.exit()

	''' Parse the web page using beautifulsoup using html.parser '''
	parsed_html=bs(page.content, 'html.parser')

	''' Find all the div tags with class item-container'''
	div_tags=parsed_html.find_all('div', class_='item-container')

	courses=list()

	''' Create a list of dictionary containing the course code, title, description and course prerequisites '''
	for course in div_tags:
		courses.append({'code':course.find_all(class_='course-annotation')[0].get_text(),'title':course.find_all(class_='course-title')[0].get_text(), 'desc':course.find_all(class_='course-desc')[0].get_text(), 'prereq':course.find_all(class_='course-prereq')[0].get_text()})

	''' Run through the list and match the course dictionary with the search term '''
	## Yes!! this can be improved. Not thought about other ways just to implement it faster.
	for it in courses:
		if(re.search(searchterm, ' '.join(it.values()))):
			print("COURSE => {}\n\t\t TITLE => {}\n\t\t DESCRIPTION => {}\n\t\t PREREQUISITE => {}\n\n".format(it['code'], it['title'], it['desc'], it['prereq']))


if(__name__ == "__main__"):
	if(len(sys.argv) > 1):
		searchterm=sys.argv[1]
		search(searchterm)
	else:
		print("Usage: python {} '<search term>'".format(sys.argv[0]))
		print("Error: Invalid number of parameters. You forgot to mention the search term")
		sys.exit()