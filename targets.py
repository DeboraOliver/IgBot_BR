
import itertools
from explicit import waiter, XPATH
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import time, random, os, csv, datetime
from selenium.webdriver.common.keys import Keys
import urllib.request, json
from flatten_json import flatten 

def get_targets(self):
    # conta alvo: uma lista de contas que pegamos nos likers de  outras instituições
    with open ('alvo.txt') as f:
        alvo = [line.rstrip () for line in f]
        print(alvo)

    # acessar uma a uma
    for account in alvo:
        self.driver.get ("https://www.instagram.com/{}/".format (account))
        time.sleep (random.uniform (5, 7))

        #Followers
        #try:
         #   allfoll = int(self.driver.find_element_by_xpath("//li[2]/a/span").text)
        #except ValueError:
        allfoll = 10


        self.driver.find_element_by_partial_link_text("follower").click()

        time.sleep(random.uniform(1.5, 2))
        trick_css = "ul div li:nth-child({}) a.notranslate"  # Taking advange of CSS's nth-child functionality

        wait = WebDriverWait(self.driver, 20)


        for group in itertools.count(start=1, step=12):
            for follower_index in range(group, group + 12):
                if follower_index > allfoll:
                    # # Load account page
                    #self.driver.get ("https://www.instagram.com/{}/".format (account))
                    #time.sleep (random.uniform (5, 7))
                    continue
                    #time.sleep (random.uniform (5, 7))
                yield waiter.find_element(self.driver, trick_css.format(follower_index)).text
            last_follower = waiter.find_element(self.driver, trick_css.format(group + 11))
            self.driver.execute_script("arguments[0].scrollIntoView();", last_follower)


def cleanse(self):


    print('Entrei no target')
    followers = []

    try:
        get_targets(self)

        #print ('\nSeguidores da conta "{}" : \n'.format (account))
        for follower in get_targets(self):
            #print(follower)
            followers.append(follower)


    finally:
        print('\n A conta tem {} seguidores'.format(len(followers)))

        print('\n Os seus seguidores são: {}'.format(followers))


        for user in followers:
            with urllib.request.urlopen ("https://www.instagram.com/{}/?__a=1".format(user)) as url:
                data = json.loads (url.read ().decode ())
                teste = flatten (data)
                print ("Estou checando o json api de cada seguidor")

                #uma nova lista
                cleaned_targets =[]
                private_account=[]
                #checar se já é nosso seguidor
                if (teste.get("graphql_user_follows_viewer")==False) and (teste.get("graphql_user_followed_by_viewer")==False):
                    if (teste.get("graphql_user_edge_followed_by_count")<999) and (teste.get("graphql_user_is_private")==False):
                        if not teste.get ("graphql_user_requested_by_viewer"):
                            cleaned_targets.append(user)
                elif (teste.get("graphql_user_is_private")==True) and (teste.get("graphql_user_profile_pic_url")!= None):
                            private_account.append(user)

        print("Há {} pessoas para interagir : {}".format(len(cleaned_targets), cleaned_targets))
        print("Há {} contas privadas: {}".format(len(private_account), private_account))

            #checar se a conta é privada
            #checar se a pessoa tem foto de perfil (não é fake)
