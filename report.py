from datetime import date, time, datetime, timedelta
import random
import interacting

def colhendo_infos(self):

    self.driver.get ('https://instagram.com')
    time.sleep (random.uniform (4.5, 6))

    interacting.scrolling(self)

    #Followers
    try:
        self.followers = int(self.driver.find_element_by_xpath("//li[2]/a/span").text)
    except ValueError:
        self.followers = self.driver.find_element_by_xpath("//li[2]/a/span").text

    #Following
    try:
        self.following = int (self.driver.find_element_by_xpath ("//li[3]/a/span").text)
    except ValueError:
        self.following = self.driver.find_element_by_xpath ("//li[3]/a/span").text

    atualizar_arquivo(self)


def atualizar_arquivo(self):

    account_name = self.account
    data_atual = datetime.now ()
    today = data_atual.strftime('%d/%m/%Y %H:%M:%S')
    followers = self.followers
    following = self.following

    report = '\n Conta: ' + account_name + 'Data: ' + today + 'Seguidores: '+followers + 'Seguindo: ' + following


    arquivo = open('work_report.txt','a')
    arquivo.write(report)
    arquivo.close()