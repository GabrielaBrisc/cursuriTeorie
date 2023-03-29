import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class ContextMenu(unittest.TestCase):
    CONTEXT = (By.ID,"hot-spot")

    ###se exe inainte de fiecare test
    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://the-internet.herokuapp.com/context_menu")

    def tearDown(self):
        self.chrome.quit()

    def test_context_menu(self):
        context_box = self.chrome.find_element(*self.CONTEXT)
        context_box.click() # facem click normal pe elem

        ### actionChains ne ajuta sa facem click dreapta
        ### alt exemplu: actionChains ne poate ajuta cand avem nevoie sa tinem apasat pe un buton
        ### si de ex in acelasi timp sa facem click
        action = ActionChains(self.chrome)

        ##met context_click ne ajuta sa def un text in care noi sa putem face click
        ## fara met de context_click nu putem accesa met perform() care executa click ul
        action.context_click(context_box).perform()
        # sleep(3)

        ##ne mutam pe alerta care a aparut si dam click pe ok
        self.chrome.switch_to.alert.accept()
        # sleep(3)