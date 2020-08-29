import itertools
from explicit import waiter, XPATH
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import time, random, os, csv, datetime
from selenium.webdriver.common.keys import Keys
import Comments

def liking(self):
    # conta alvo: uma lista de contas que pegamos nos likers de  outras instituições
    with open ('alvo.txt') as f:
        alvo = [line.rstrip () for line in f]
        print(alvo)

    # acessar uma a uma
    for potencial_user in alvo:
        self.driver.get ("https://www.instagram.com/{}/".format (potencial_user))
        time.sleep (random.uniform (5, 7))
        #entrar na página pessoal

        # Ultima foto do feed
        pic = self.driver.find_element_by_class_name ("_9AhH0")

        pic.click ()
        time.sleep (random.uniform (3, 5.5))

        # quantos likes vamos dar
        amei = 0

        while amei < 3:
            # liking
            like = self.driver.find_element_by_xpath ('/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button')
            like.click ()
            amei += 1
            print ("Dei like")
            time.sleep (random.uniform (2, 2.5))


            # COMMENT
            if amei % 2 == 0 and amei != 0:
                Comments.commenting(self)

            # PROXIMA FOTO
            next = self.driver.find_element_by_partial_link_text ('Next')
            next.click ()
            time.sleep (random.uniform (2, 4.5))
