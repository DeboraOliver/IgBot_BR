
import itertools
from explicit import waiter, XPATH
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import time, random, os, csv, datetime
from selenium.webdriver.common.keys import Keys

def list_followers(self, account):
    #profile
    self.driver.get("https://www.instagram.com/{0}/".format(account))
    time.sleep(random.uniform(5, 7))
    #Followers

    allfoll = int(self.driver.find_element_by_xpath("//li[2]/a/span").text)
    self.driver.find_element_by_partial_link_text("follower").click()

    time.sleep(random.uniform(1.5, 2))
    trick_css = "ul div li:nth-child({}) a.notranslate"  # Taking advange of CSS's nth-child functionality

    wait = WebDriverWait(self.driver, 20)


    for group in itertools.count(start=1, step=12):
        for follower_index in range(group, group + 12):
            if follower_index > allfoll:
                # # Load account page
                next
                #raise StopIteration

                #time.sleep (random.uniform (5, 7))
            yield waiter.find_element(self.driver, trick_css.format(follower_index)).text

            #followers.append(waiter.find_element(driver, trick_css.format(follower_index)).text)
        #https://stackoverflow.com/questions/37233803/how-to-web-scrape-followers-from-instagram-web-browser
        # Instagram loads followers 12 at a time. Find the last follower element
        # and scroll it into view, forcing instagram to load another 12
        # Even though we just found this elem in the previous for loop, there can
        # potentially be large amount of time between that call and this one,
        # and the element might have gone stale. Lets just re-acquire it to avoid
        # that
        last_follower = waiter.find_element(self.driver, trick_css.format(group + 11))
        self.driver.execute_script("arguments[0].scrollIntoView();", last_follower)




def list_following(self.driver):

# following = []
    time.sleep(random.uniform(3, 6))
# # Load account page
    #driver.get("https://www.instagram.com/{0}/".format(account))
   # time.sleep(random.uniform(5, 7))
    trick_css = "ul div li:nth-child({}) a.notranslate"  # Taking advange of CSS's nth-child functionality
# # Click the 'Following' link

    allfow = int(self.driver.find_element_by_xpath("//li[3]/a/span").text)
    self.driver.find_element_by_partial_link_text("following").click()
    time.sleep(random.uniform(4, 6))
#
    for group1 in itertools.count(start=1, step=12):
        for following_index in range(group1, group1 + 12):
            if following_index > allfow:
                raise StopIteration
            yield waiter.find_element(self.driver, trick_css.format(following_index)).text
#             following.append(waiter.find_element(self.driver, trick_css.format(following_index)).text)
#         else:
#             raise StopIteration
        last_following = waiter.find_element(self.driver, trick_css.format(group1 + 11))
        self.driver.execute_script("arguments[0].scrollIntoView();", last_following)

def celebs_to_keep(self.driver):
# #lista de celebridades que eu ligo e não quero que sai da lista

	celebs_to_keep = 'natgeo'
	followers.extend(celebs_to_keep)
	following = [x for x in following if x not in celebs_to_keep]

# #vamos comparar as duas listas criadas e unfollow quem  não nos segue

	to_unfollow = [i for i in following if i not in followers]

	print(to_unfollow)

 #vamos entrarno perfil de cada uma e dar um unfollow
	unfollowed = 0

	while unfollowed <= 3:
		for notfollowingme in to_unfollow:
			self.driver.get("https://www.instagram.com/{0}/".format(notfollowingme))
			time.sleep (random.uniform (3, 5))
			self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button').click()
			time.sleep (random.uniform (2, 4)
			self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()
			unfollowed += 1
			to_unfollow.remove(notfollowingme)
			time.sleep (random.uniform (2.5, 3.5))



if __name__ == "__main__":

    account = 'dina_agencia_digital'

    print ('\nEste programa dá unfollowing "{}" \n'.format(account))
    dirpath = os.getcwd ()
    print ("current directory is : " + dirpath)
    chromepath = dirpath + '/assets/chromedriver.exe'

    # retiraras notificações
    chrome_options = webdriver.ChromeOptions ()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option ("prefs", prefs)
    driver = webdriver.Chrome (executable_path=chromepath, options=chrome_options)

    followers = []
    following = []

    try:
        login(self.driver,account)

        #print ('\nSeguidores da conta "{}" : \n'.format (account))
        for follower in list_followers(self.driver, account=account):
            #print(follower)
            followers.append(follower)

        for following1 in list_following(self.driver, account=account):
            #print(follower)
            following.append(following1)

    finally:
        print('\n A conta {} tem {} seguidores'.format(account,len(followers)))

        print('\n Os seus seguidores são: {}'.format(followers))


        print ('\n A conta {} segue {} contas'.format (account, len (following)))

        print ('\n Quem você segue: {}'.format(following))