import time 
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup



class LinkPage:
    def __init__(self):
        self.login_url:str= "https://linkedin.com/uas/login"
        self.credentials_path:str="..\\utils\credentials.json"
        self.wdrive= None
    #authenticate 
    def profile_auth(self):
        """module used to make authentication on linkedin page

        Parameters
        ----------
        credentials : dict, optional
            dict containg username and password by default None

        Returns
        -------
    
        execute the authentication and return a webdriver authenticated on linkedin
        """
        #get credentials
        
        with open(f'{self.credentials_path}', 'r') as f:
            credentials = json.load(f)  

        #creating web browser intance
        driver = webdriver.Chrome()
        #openning linkedin page
        driver.get(self.login_url)
        #waiting for the page to load
        time.sleep(5)
        # select username form
        username = driver.find_element(value='username')
        #Enter user adress
        username.send_keys(credentials['username'])
        #select password form
        pword = driver.find_element(value='password')
        #enter password
        pword.send_keys(credentials['pword'])

        # Clicking on the log in button
        # Format (syntax) of writing XPath -->
 
        driver.find_element(by=By.XPATH,value='//button[@type="submit"]').click()
        print("="*80)
        print("sucefully logged!")
        self.wdrive = driver
        return driver
    