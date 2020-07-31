import itertools
from explicit import waiter, XPATH
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import time, random, os, csv, datetime
from selenium.webdriver.common.keys import Keys


def login(driver, account):
    driver.get ('https://instagram.com')
    time.sleep (random.uniform (5, 7))

    # information
    archive = open ('important.txt', 'r')
    token = archive.read ()

    # username
    username = driver.find_element_by_xpath (
        '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
    username.send_keys (account)

    # senha
    password = driver.find_element_by_xpath (
        '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
    password.send_keys (token)
    # clicar no botão loging
    submit = driver.find_element_by_xpath ('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]')
    submit.click ()
    time.sleep (random.uniform (5, 7))

    # Wait for the user dashboard page to load
    WebDriverWait (driver, 15).until (EC.presence_of_element_located ((By.LINK_TEXT, "See All")))


def list_followers(driver, account):
    # profile
    driver.get ("https://www.instagram.com/{0}/".format (account))
    time.sleep (random.uniform (1.5, 2))
    # Followers

    allfoll = int (driver.find_element_by_xpath ("//li[2]/a/span").text)
    driver.find_element_by_partial_link_text ("follower").click ()

    time.sleep (random.uniform (1.5, 2))
    trick_css = "ul div li:nth-child({}) a.notranslate"  # Taking advange of CSS's nth-child functionality

    wait = WebDriverWait (driver, 20)

    for group in itertools.count (start=1, step=12):
        for follower_index in range (group, group + 12):
            if follower_index > allfoll:
                raise StopIteration
            yield waiter.find_element (driver, trick_css.format (follower_index)).text

            # followers.append(waiter.find_element(driver, trick_css.format(follower_index)).text)
        # https://stackoverflow.com/questions/37233803/how-to-web-scrape-followers-from-instagram-web-browser
        # Instagram loads followers 12 at a time. Find the last follower element
        # and scroll it into view, forcing instagram to load another 12
        # Even though we just found this elem in the previous for loop, there can
        # potentially be large amount of time between that call and this one,
        # and the element might have gone stale. Lets just re-acquire it to avoid
        # that
        last_follower = waiter.find_element (driver, trick_css.format (group + 11))
        driver.execute_script ("arguments[0].scrollIntoView();", last_follower)



if __name__ == "__main__":

    account = 'dina_agencia_digital'

    print ('\nBem-vinda! Entrando na conta "{}" \n'.format (account))
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
        login (driver, account)

        # print ('\nSeguidores da conta "{}" : \n'.format (account))
        for follower in list_followers (driver, account=account):
            # print(follower)
            followers.append (follower)

    finally:
        print ('\n A conta {} tem {} seguidores'.format (account, len (followers)))

        print ('\n Os seus seguidores são: {}'.format (followers))
        driver.quit ()





