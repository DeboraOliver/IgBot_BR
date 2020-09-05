import itertools
from explicit import waiter, XPATH
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import time, random, os, csv, datetime
from selenium.webdriver.common.keys import Keys
import Like as lk
import targets


class IgBot:

    def __init__(self, account):

        print ("\nBem-vinda! Vamos começar?! \n")
        dirpath = os.getcwd ()
        print ("current directory is : " + dirpath)
        chromepath = dirpath + '/assets/chromedriver.exe'

        # it will disable any unexpected notification
        chrome_options = webdriver.ChromeOptions ()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option ("prefs", prefs)
        self.driver = webdriver.Chrome (executable_path=chromepath, options=chrome_options)

        self.account = account
        self.login()

    def login(self):



        self.driver.get('https://instagram.com')
        time.sleep(random.uniform(5, 7))

        #information
        archive = open('important.txt','r')
        token = archive.read()


        # username
        username = self.driver.find_element_by_name('username')
        username.send_keys(self.account)

        # senha
        password = self.driver.find_element_by_name('password')
        password.send_keys(token)
        # clicar no botão loging
        submit = self.driver.find_element_by_id('loginForm')
        submit.click()
        time.sleep(random.uniform(5, 7))

        #pagina perguntando sobre salva a senha

        # Wait for the user dashboard page to load
        #Webself.driverWait(self.driver, 15).until(EC.presence_of_element_located((By.LINK_TEXT, "See All")))
        #<button class="sqdOP yWX7d     _8A5w5    " type="button"><span>6</span> others</button>


        self.driver.get ("https://www.instagram.com/{0}/".format (self.account))
        time.sleep (random.uniform (5, 7))

        # LIKERS
        #lk.liking(self)
        print('era p o cleanse começar')
        targets.cleanse(self)

if __name__ == "__main__":

    account = 'dina_agencia_digital'

    IgBot(account)
    print('terminei o principal')
 

        #self.driver.quit ()





