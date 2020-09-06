import random
import time


# Neste aquivo ficam as funções que evitam de sermos bloqueados


# ir até a home
def home_scroll(self):
    try:
        self.driver.find_element_by_partial_link_text ("Home").click ()
        self.driver.execute_script ("window.scrollTo(0, 1080)")
        time.sleep (random.uniform (4, 6))
        self.driver.execute_script ("window.scrollTo(1080, 0)")
    except:
        self.driver.get ('https://instagram.com')
        time.sleep (random.uniform (2, 5))


# olhando a pagina
def scrolling(self):
    self.driver.execute_script ("window.scrollTo(0, 1080)")
    time.sleep (random.uniform (3, 5.5))
    self.driver.execute_script ("window.scrollTo(1080, 0)")
    time.sleep (random.uniform (3.5, 6.5))


# meu inbox
def inbox(self):
    self.driver.get ('https://www.instagram.com/direct/inbox/')
    time.sleep (random.uniform (2, 3))

    # explore

def explore_tag(self):
    self.driver.get ('https://www.instagram.com/explore/')
    self.driver.execute_script ("window.scrollTo(0, 1080)")
    time.sleep (random.uniform (5, 6.5))
    self.driver.execute_script ("window.scrollTo(1080, 0)")
    time.sleep (random.uniform (3, 5))

# stories
