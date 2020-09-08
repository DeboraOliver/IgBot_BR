
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
import interacting
import Like
import Comments

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
                    break #TEM ERRO AQUI
                    #time.sleep (random.uniform (5, 7))
                yield waiter.find_element(self.driver, trick_css.format(follower_index)).text
            last_follower = waiter.find_element(self.driver, trick_css.format(group + 11))
            self.driver.execute_script("arguments[0].scrollIntoView();", last_follower)


def cleanse(self):


    print('Entrei no target')
    followers = []
    # uma nova lista
    self.cleaned_targets = []
    self.private_account = []
    cleaned_targets = 0
    private_account = 0

    try:
        get_targets(self)

        #print ('\nSeguidores da conta "{}" : \n'.format (account))
        for follower in get_targets(self):
            #print(follower)
            followers.append(follower)
            with urllib.request.urlopen ("https://www.instagram.com/{}/?__a=1".format(follower)) as url:
                data = json.loads (url.read ().decode ())
                flat_json = flatten (data)

                #checar se já é nosso seguidor
                if (flat_json.get("graphql_user_edge_followed_by_count")<999) and (flat_json.get("graphql_user_edge_owner_to_timeline_media_count")>3):
                    if (flat_json.get ("graphql_user_follows_viewer") == False) and (flat_json.get ("graphql_user_followed_by_viewer") == False):
                        if not flat_json.get ("graphql_user_requested_by_viewer"):
                            self.cleaned_targets.append(follower)
                            cleaned_targets += 1
                            print("Nossos futuros seguidores: {}".format(cleaned_targets))
                elif (flat_json.get("graphql_user_is_private")==True) and (flat_json.get("graphql_user_edge_followed_by_count")<999):
                            self.private_account.append(follower)
                            private_account += 1
                            print ("Número de contas privadas: {}".format(private_account))


    finally:
        print('\n A conta tem {} seguidores'.format(len(followers)))

        print('\n Os seus seguidores são: {}'.format(followers))

        print("Há {} pessoas para interagir : {}".format(len(self.cleaned_targets), self.cleaned_targets))
        print("Há {} contas privadas: {}".format(len(self.private_account), self.private_account))

def like_each(self):
    Like.liking(self)

