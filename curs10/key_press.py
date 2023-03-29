import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


class Keyboard(unittest.TestCase):

    INPUT_FIRST_NAME = (By.ID,"first-name")
    INPUT_LAST_NAME = (By.ID,"last-name")

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://formy-project.herokuapp.com/form")

    def tearDown(self):
        self.chrome.quit()

    def test_pressing_keys(self):
        first_name  = self.chrome.find_element(*self.INPUT_FIRST_NAME)

        first_name.send_keys("Gabriela")
        # sleep(3)

        first_name.send_keys(Keys.BACK_SPACE)
        # sleep(3)

        first_name.send_keys(Keys.TAB)
        # sleep(3)

        ### ne fol de ACtionChanins pt a tine apasat o tasta si apoi a apasa o alta tasta
        action = ActionChains(self.chrome)
        ## fol kew_down pt a tine apasat o tasta (SHIFT in acest caz)
        action.key_down(Keys.SHIFT).perform()

        ##apasam pe tasta TAB
        action.send_keys(Keys.TAB)

        ##fol key_up pt a da drumul la tasta (SHIFT)
        ## daca nu punem si aceasta instr si am fol key_down nu v-a functiona
        action.key_up(Keys.SHIFT).perform()
        # sleep(3)
        first_name.send_keys(Keys.BACK_SPACE)
        # sleep(4)
