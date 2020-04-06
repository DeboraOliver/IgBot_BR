'''Let's play around with seleniumpackage to access our page'''


import time, random, os, csv, datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

print("\nBem-vinda! Vamos começar?! \n")
dirpath = os.getcwd()
print("current directory is : " + dirpath)
chromepath = dirpath + '/assets/chromedriver.exe'

driver = webdriver.Chrome(executable_path=chromepath)

driver.get('https://instagram.com')

# username
usernamebox = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
usernamebox.send_keys('dina_agencia_digital')
# senha
passwordbox = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
passwordbox.send_keys('Ig123456!')
# clicar no botão loging
loginbutton = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]')
loginbutton.click()

time.sleep(random.uniform(1.5, 3.5))


# ir ao final da página
def load_page(self, sleep=1):
    scroll_page = 0
    while scroll_page < 4000:
        self.browser.execute_script("window.scrollTo(0," + str(scroll_page) + " );")
        scroll_page += 200
        print('rolagem ok!')
        time.sleep(sleep)


# ir no meu perfil
myprofile = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/a/img')
myprofile.click()
print('Profile ok')
time.sleep(random.uniform(2.5, 4.5))

# lista seguidores
my_followers_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
my_followers_button.click()
print('seguidores  ok')
my_followers = []
my_followers = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
print(my_followers)

# listar quem seguimos

# na minha ultima postagem pegar os likes e visitar duas pessoas

# voltar a minha página inicial
firstpage = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a/svg/path')
firstpage.click()

# listar as pessoas que quero seguir
targets = ['influenciadoradesucesso', 'escoladeinfluencers', 'influencianegra', 'empreendedorinfluencer',
           'empreendedorasbrilhantes']

'''GRANDE LOOP'''
for target in targets:
    # digitar o  nome que quero na pagina de pesquisa
    searchbox = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div')
    searchbox.send_keys(target)
    # pressionar o enter

    # ir até o final da página
    driver.execute_script("window.scrollTo(0,2*127)")
    time.sleep(random.uniform(2.5, 3.5))

# olhar a última postagem
last_post = driver.find_element_by_xpath(
    '//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]')
last_post.click()
time.sleep(random.uniform(4.5, 6))

last_post_likers = driver.find_element_by_xpath(
    '/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div[2]/button')
last_post_likers.click()
time.sleep(random.uniform(1.5, 2))

# listar quem deu like na ultima foto da pessoa
target_followers = []

'''SEGUNDO GRANDE LOOP'''
# visitar quem deu like
# SE perfil private == ADD
# SE SEM FOTO == NEXT
# SE NUMERO DE POSTS <=5 == NEXT
# SE numero de followers >=5000 NEXT
# SE Numero de followers <=100 DAR LIKE E COMENTAR
# dar like
# escrever comentário
# add




#

# with webdriver.Firefox() as driver:
#   wait = WebDriverWait(driver, 10)
#  driver.get("https://google.com/ncr")
