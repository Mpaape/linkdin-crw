import time 
import json
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from auth import profile_auth

#login
driver = profile_auth()

#extract data
# Opening Kunal's Profile
# paste the URL of Kunal's profile here
profile_url = "https://www.linkedin.com/in/mateus-magnus-paape-1a96797b/"
driver.get(profile_url)        # this will open the link

 start = time.time()

# will be used in the while loop
initialScroll = 0
finalScroll = 1000

while True:
	driver.execute_script(f"""window.scrollTo({initialScroll},
											{finalScroll})
						""")
	# this command scrolls the window starting from
	# the pixel value stored in the initialScroll
	# variable to the pixel value stored at the
	# finalScroll variable
	initialScroll = finalScroll
	finalScroll += 1000

	# we will stop the script for 3 seconds so that
	# the data can load
	time.sleep(3)
	# You can change it as per your needs and internet speed

	end = time.time()

	# We will scroll for 20 seconds.
	# You can change it as per your needs and internet speed
	if round(end - start) > 20:
		break


src = driver.page_source
 
# Now using beautiful soup
def get_xml():
 return profile_soup = BeautifulSoup(src, 'lxml')


def get_info(): 
#Extracting Profile Introduction:
intro = soup.find('div', {'class': 'pv-text-details__left-panel'})

name = soup.find('h1', class_='text-heading-xlarge').text
title = soup.find('div', class_='text-body-medium').text




 