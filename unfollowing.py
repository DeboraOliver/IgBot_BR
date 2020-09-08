
import itertools
import json
import random
import time
import urllib.request
import interacting
from explicit import waiter
from flatten_json import flatten


def list_following(self):


    trick_css = "ul div li:nth-child({}) a.notranslate"  # Taking advange of CSS's nth-child functionality
    #allfow = int(self.driver.find_element_by_xpath("//li[3]/a/span").text)

    #a cada 20 vamos checar quem nos segue de volta
    allfow= 20

    self.driver.find_element_by_partial_link_text("following").click()
    time.sleep(random.uniform(4, 6))


    #
    for group1 in itertools.count(start=1, step=12):
        for following_index in range(group1, group1 + 12):
            if following_index > allfow:
                break
            yield waiter.find_element(self.driver, trick_css.format(following_index)).text
        #             following.append(waiter.find_element(self.driver, trick_css.format(following_index)).text)
        #         else:
        #             raise StopIteration
        last_following = waiter.find_element(self.driver, trick_css.format(group1 + 11))
        self.driver.execute_script("arguments[0].scrollIntoView();", last_following)



def cleanse(self):

    print('Entrei no  unfollowing  mode')
    nonfollowers = []
    # uma nova lista
    self.unfollow_me = []

    unfollowing = 0


    try:
        list_following (self)


        for unfollow in list_following(self):
            nonfollowers.append (unfollow)
            with urllib.request.urlopen ("https://www.instagram.com/{}/?__a=1".format (unfollow)) as url:
                data = json.loads (url.read ().decode ())
                flat_list = flatten (data)

                # checar se já é nosso seguidor
                if not flat_list.get ("graphql_user_follows_viewer") == False:
                    self.unfollow_me.append (unfollow)
                    unfollowing += 1
                    print ("Deixarei de seguir: {}".format (unfollowing))



    finally:


        print ("Deixaremos de seguir : {}".format (len (self.unfollow_me), self.unfollow_me))

        celebs_to_keep(self)


def celebs_to_keep(self):
    # #lista de celebridades que eu ligo e não quero que sai da lista
    with open ('celebridades.txt') as f:
        celebs = [line.rstrip () for line in f]
        print ("Vamos manter estas celebridades: {}".format (celebs))

        #celebs_to_keep = 'natgeo'

        #followers.extend (celebs_to_keep)
        #following = [x for x in following if x not in celebs_to_keep]

        # #vamos comparar as duas listas criadas e unfollow quem  não nos segue

        self.to_unfollow = [i for i in self.unfollow_me if i not in celebs]

        unfollowing(self)

def unfollowing(self):

    unfollowed = 0

    while unfollowed <= 3:
        for notfollowingme in self.to_unfollow:
            self.driver.get("https://www.instagram.com/{0}/".format(notfollowingme))
            interacting.scrolling(self)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button').click()
            time.sleep (random.uniform (2, 4))
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()
            unfollowed += 1
            self.to_unfollow.remove(notfollowingme)
            time.sleep (random.uniform (2.5, 3.5))


