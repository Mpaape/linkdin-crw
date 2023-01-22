import time 
import json
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

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
        self.languages = None
        self.soup = None
        self.data={}

    def get_name(self):
        name = self.soup.find('h1', class_='text-heading-xlarge')
        if name is not None:
            self.name = name.text

    def get_title(self):
        title = self.soup.find('div', class_='text-body-medium').text
        if title is not None:
            self.title = re.sub(r'^\s+|\s+$', '', title)

    def get_image_path(self):
        topcard = self.soup.find('section',"artdeco-card ember-view pv-top-card")
        img = topcard.find(class_="pv-top-card-profile-picture__image pv-top-card-profile-picture__image--show ember-view")
        if img is not None:
            self.image_path=img.attrs['src']
        
    def get_premium(self):
         topcard = self.soup.find('section',"artdeco-card ember-view pv-top-card")
         if topcard.find("span",class_="pv-member-badge pv-member-badge--for-top-card") is not None:
            self.premium = True
         self.premium = False

    def get_current_job(self):
        topcard = self.soup.find('section',"artdeco-card ember-view pv-top-card")
        self.current_job=topcard.find('ul').find('li').find('button').attrs['aria-label'].split(':')[1].split('.')[0]
        
    def get_location(self):
        topcard = self.soup.find('section',"artdeco-card ember-view pv-top-card")
        location = topcard.find('span', class_="text-body-small inline t-black--light break-words").text
        self.location = re.sub(r'^\s+|\s+$', '', location)
    
    def get_conections(self):
        self.conections = self.soup.find("ul", class_="pv-top-card--list pv-top-card--list-bullet").find("li").find("span", class_="t-bold").text
      
    def get_about(self):
        about_card = self.soup.find('div',class_='display-flex ph5 pv3')
        if about_card is not None:
            self.about = re.sub(r'^\s+|\s+$', '', about_card.text)
        
    def get_experience(self):
        experience= (        
            self.soup
                .find("div",{"class":"pv-profile-card-anchor"},id="experience")
                .find_next("span") 
                .find_next("ul").text
        )
        if experience is not None:
            experience_soup = ' '.join(experience.splitlines())
            experience_soup=experience_soup.split("…ver mais")
            experience_soup = [i.strip() for i in experience_soup]
            self.experience={f"experience_{i+1}": experience_soup[i] for i in range(len(experience_soup))}

    def get_education(self):
        education = (
            self.soup
                .find("div",{"class":"pv-profile-card-anchor"},id="education")
                .find_next("span") 
                .find_next("ul").text
        ) 
        if education is not None:
            education_soup = ' '.join(education.splitlines())
            educations = [ i.strip() for i in education_soup.split("…ver mais")]
            self.education={f"education_{i+1}": educations[i] for i in range(len(educations))}
      
    def get_certifications(self):
        certifications = (
            self.soup
                .find("div",{"class":"pv-profile-card-anchor"},id="licenses_and_certifications")
                .find_next("span") 
                .find_next("ul").text
        ) 
        if certifications is not None:
            certifications_soup = ' '.join(certifications.splitlines())
            certifications_soup = certifications_soup.split("Exibir credencial")
            certifications_soup = [i.strip() for i in certifications_soup]
            self.certifications={f"certification_{i+1}": certifications_soup[i] for i in range(len(certifications_soup))}
        
    def get_skills(self):
        skills_soup  = (
            self.soup
                .find("div",{"class":"pv-profile-card-anchor"},id="skills")
                .find_next("span") 
                .find_next("ul").text
        )
        def _format_skill(soup_txt):
            #should be removed of string
            cut_lin = ' competências'
            #make a list without
            join_list = ''.join(soup_txt.splitlines())
            #remmoved
            join_list =[i.split("  ")[0]  for i in join_list.split("recomendações de") if i != cut_lin]

            skills_dict = {}
            
            for item in range(len(join_list)):
                if item %2 ==0:
                    if item < len(join_list) :
                        size_string = len(join_list[item])
                        pattern =re.compile("^ competências")
                        string_dedup = pattern.sub("", join_list[item])
                        size_string = len(string_dedup)
                        string_dedup = string_dedup[:size_string//2]                      
                        skills_dict[string_dedup] = re.sub('[^0-9]', '', join_list[item+1] )      
            return skills_dict
        if skills_soup is not None:
            self.skills=_format_skill(skills_soup)


    def get_languages(self):
        soup_txt  = (
            self.soup
                .find("div",{"class":"pv-profile-card-anchor"},id="languages")
                .find_next("span") 
                .find_next("ul").text
        )
        def _format_lg(soup_txt):
            #should be removed of string
            cut_lin = ['intermediário','básico','avançado','Nível']
            #make a list without
            join_list = ''.join(soup_txt.splitlines()).split()
            #remmoved
            join_list =[i.split("Nível")[0] for i in join_list if i not in cut_lin]
            languages_dict = {}
            
            for item in range(len(join_list)):
                if item %2 ==0:
                    if item < len(join_list) :
                        size_string = len(join_list[item])
                        string_dedup = join_list[item][:size_string//2]
                        languages_dict[string_dedup] = join_list[item+1]
            return languages_dict   
        if soup_txt is not None:    
            self.languages = _format_lg(soup_txt)
       
    def get_all_profile(self):
        self.url= self.url
        self.get_name()
        self.get_title()
        self.get_current_job()
        self.get_location()
        self.get_conections()
        self.get_premium()
        self.get_image_path()
        self.get_about()
        self.get_experience()
        self.get_education()
        self.get_certifications()
        self.get_skills()
        self.get_languages()
        self.to_dict()

    def to_dict(self):
        self.data['url'] = self.url
        self.data['name'] = self.name
        self.data['title'] = self.title
        self.data['current_job'] =  self.current_job
        self.data['location'] = self.location
        self.data['conections'] = self.conections
        self.data['premium'] = self.premium
        self.data['image_path'] = self.image_path
        self.data['about'] = self.about
        self.data['experience'] = self.experience
        self.data['education'] = self.education
        self.data['certifications'] = self.certifications
        self.data['skills'] = self.skills
        self.data['languages'] = self.languages
        #self.data['soup'] = str(self.soup)
        return self.data

 
 

    