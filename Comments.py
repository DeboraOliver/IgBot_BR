import itertools
from explicit import waiter, XPATH
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import time, random, os, csv, datetime
from selenium.webdriver.common.keys import Keys
import random


# Comentando
def commenting(self):
    comments = ['Maravilhosxxx! @{}',
                'Amei! @{}',
                'Adorei :thumbsup:',
                'Que incrível :open_mouth:',
                'Que camera você usa @{}?',
                'TOP @{}',
                'Que lindxxxx @{}',
                ':raised_hands:',
                ':raised_hands: Perfeito!',
                ' @{} ']

    texto_do_comentario = random.choice (comments)
    print ('Vou postar: "{}"'.format(texto_do_comentario))

    comment_area = self.driver.find_element_by_css_selector ('form  textarea') #deu erro
    comment_area.send_keys (texto_do_comentario)
    time.sleep (random.uniform (2, 3.5))

    post_comment = self.driver.find_element_by_xpath ('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button')
    post_comment.click ()
    print('Comentei: {}'.format(texto_do_comentario))
    time.sleep (random.uniform (5, 6))