import time 
import json
import random 

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


class LinkBot:
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
        rand = random.randint(1,3)
        time.sleep(5+rand)
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
        print("logged!")
        self.wdrive = driver
        return driver
    
    def get_soup(self,url):
        ''' makes a scan over linkedin profile ''' 
        profile_url = url
        driver = self.wdrive
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
            rand = random.randint(1,3)
            time.sleep(5+rand)
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