import time 
import json
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

 
from crawler import LinkPage


class Profile:
    def __init__(self,url=None):
        self.url = url
        self.name =None
        self.title = None
        self.image_path= None
        self.premium = None
        self.current_job = None
        self.location = None
        self.conections = None
        self.about = None
        self.experience = None
        self.education = None
        self.certifications= None
        self.skills = None
        self.lenguages = None
        self.soup = None
        self.data={}

    def get_name(self):
        self.name = self.soup.find('h1', class_='text-heading-xlarge').text
       
    def get_title(self):
        title = self.soup.find('div', class_='text-body-medium').text
        self.title = re.sub(r'^\s+|\s+$', '', title)

    def get_image_path(self):
        topcard = self.soup.find('section',"artdeco-card ember-view pv-top-card")
        self.image_path=topcard.find(class_="pv-top-card-profile-picture__image pv-top-card-profile-picture__image--show ember-view").attrs['src']
    
    def get_premium(self):
         topcard = self.soup.find('section',"artdeco-card ember-view pv-top-card")
         if top_card.find("span",class_="pv-member-badge pv-member-badge--for-top-card") is not None:
            self.premium = True
         self.premium = False

    def get_current_job(self):
        topcard = self.soup.find('section',"artdeco-card ember-view pv-top-card")
        self.current_job=topcard.find('ul').find('li').find('button').attrs['aria-label'].split(':')[1].split('.')[0]
        
    def get_location(self):
        topcard = self.soup.find('section',"artdeco-card ember-view pv-top-card")
        location = top_card.find('span', class_="text-body-small inline t-black--light break-words").text
        self.location = re.sub(r'^\s+|\s+$', '', location)
    
    def get_conections(self):
        self.conections = soup.find("ul", class_="pv-top-card--list pv-top-card--list-bullet").find("li").find("span", class_="t-bold").text
      
    def get_about(self):
        about_card = self.soup.find('div',class_='display-flex ph5 pv3')
        self.about = re.sub(r'^\s+|\s+$', '', about_card.text)
        
    def get_experience(self):
        pass

    def get_education(self):
      pass
        
    def get_certifications(self):
       pass
        
    def get_skills(self):
       pass
    def get_languages(self):
       pass
    def to_dict(self):
        self.data['name'] = self.name
        self.data['title'] = self.title
        self.data['location'] = self.location
        self.data['conections'] = self.conections
        self.data['about'] = self.about
        self.data['experience'] = self.experience
        self.data['education'] = self.education
        self.data['certifications'] = self.certifications
        self.data['skills'] = self.skills
        self.data['languages'] = self.languages
        return self.data


def get_soup(webdriver,url): 
    
    profile_url = url
    driver.get(profile_url) 

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
    def get_xml(src):
        return BeautifulSoup(src, 'lxml')

    return get_xml(src)


#login
driver = LinkPage().profile_auth()
#url = "https://www.linkedin.com/in/dianechiang/"
url = "https://www.linkedin.com/in/carlos-fernandes91/"

soup =get_soup(webdriver=driver, url=url)

prof=Profile(url)
prof.soup = soup




prof.get_name()
print(prof.name)

prof.get_conections()
print(prof.conections)

prof.get_title()
print(prof.title)

prof.get_current_job() 
print(prof.current_job)

prof.get_image_path()
print(prof.image_path)


top_card=soup.find('section',"artdeco-card ember-view pv-top-card") 
top_card.find("span",class_="pv-member-badge pv-member-badge--for-top-card")
 
#tags
uls = [re.sub(r'^\s+|\s+$', '', i.text) for i in soup.find_all("ul")]  

a_string = soup.find(string="Idiomas")
a_string
# u'Lacie'

soup.select(".Idiomas")
