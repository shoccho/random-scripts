#!/usr/bin/env python3

import requests as req
from bs4 import BeautifulSoup


user_agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

login_page = "https://ideone.com/account/login"
myrecent = "https://ideone.com/myrecent"

login_data = {
	'username' : '',
	'password' : '',
	'remember' : 'yes',
	'next' : 'login_key'
}


with req.Session() as session:

	# opening login page
	rq = session.get(login_page, headers=user_agent)
	soup = BeautifulSoup(rq.content, features="html.parser")

	# login info
	login_data['username'] = input('username - ')
	login_data['password'] = input('password - ')

	# getting password hash or next code
	login_data['next'] = soup.find('input', attrs={'name':'next'}).get('value')
	
	# we just loged in	
	rq = session.post(login_page, data=login_data, headers=user_agent)
	soup = BeautifulSoup(rq.content, features="html.parser")

	# accessing 'my recent' page
	rq = session.get(myrecent, headers=user_agent)
	soup = BeautifulSoup(rq.content, features="html.parser")

	uls = soup.find_all("ul", class_= "dropdown-menu")
	#print(uls[0].findChildren())
	lis = uls[1].findChildren()
	
	#traverse the dropwown menu
	
	for li in lis:
		li['class']="active"
		#selecting a page here 
	
		print(li)
		#set the active tag back to null
		li['class']=""
	print(soup.prettify())


	fp = open("test.html", "w")
	fp.write(soup.prettify())
	fp.close()


