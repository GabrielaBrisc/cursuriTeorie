# import unittest   #importam libraria unitest care va face programul in bugati rulabile individual
# from telnetlib import EC
# from time import sleep
# from unittest import TestCase
#
# from selenium import webdriver
# from selenium.common import NoSuchElementException
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import unittest
from unittest import TestCase

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random


chrome  = webdriver.Chrome()

class Login(TestCase):
    H2_ELEMENT_XPATH = (By.XPATH,"//*[@id='content']/h2")
    LOGIN_BUTTON = (By.XPATH, "//i[@class='fa fa-2x fa-sign-in']")
    ERROR_MESSAGE = (By.XPATH,"//div[normalize-space(contains(text(),'Your username is invalid'))]")
    ATRIBUT_HREF = (By.XPATH,"//a[@href='http://elementalselenium.com/']")
    JOB_TITLE = (By.ID,"job-title")

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://the-internet.herokuapp.com/login")
        # * tuple unpacking -  se ia valoarea din tuple si se da ca argument functiei
        # self.chrome.find_element(By.XPATH, "//*[@id='content']/h2").is_displayed()
        # Daca nu facem unpack functia ar arata asa find_element((By.LINK_TEXT,"Form"))
        # Daca facem unpack functia ar arata asa fin_element(By.LINK_TEXT,"Form")
    def tearDown(self):
        self.chrome.quit()
###
    # @unittest.skip
    def test_url(self):
        actual_url = self.chrome.current_url
        expected_url = "https://the-internet.herokuapp.com/"
        assert actual_url == expected_url, f"Valid URL."

## ● Test 2
## - Verifică dacă page title e corect
    # @unittest.skip
    def test_page_title(self):
        actual_title = self.chrome.title
        expected_title = "The Internet"
        assert actual_title == expected_title, f"Valid Title"
        ##sau
        ###self.assertEqual(expected, actual,  f' Titlul paginii este {actual}, dar ar fi trebuit sa fie {expected}')
        sleep(2)

# ##   Test 3
# ## - Verifică textul de pe elementul xpath=//h2 e corect
# ## - da failed
#     @unittest.skip
    def test_element(self):
        self.chrome.get("https://the-internet.herokuapp.com/")
        actual_element = self.chrome.find_element(*self.H2_ELEMENT_XPATH)
        expected_element = "Available Examples"
        # assert  actual_element == expected_element, f"elementul este {expected_element}"
        self.assertEqual(actual_element, expected_element, f"elementul este {actual_element}")

### Test 4
# - Verifică dacă butonul de login este displayed
    ##elementul nu este gasit, nu avem buton de login pe aceasta pg
#     @unittest.skip
    def test_Login_button(self):
        self.chrome.get("https://the-internet.herokuapp.com/")
        try:
           self.chrome.find_element(*self.LOGIN_BUTTON)
           assert False, "Elementul a fost gasit"
        except NoSuchElementException:
            print("Elementul nu este afisat")
#
# ### Test 5
# ##  - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect
#     @unittest.skip
    def test_Atribut_href(self):
        self.chrome.get("https://the-internet.herokuapp.com/")
        # actual_atribut = self.chrome.find_element(*self.ATRIBUT_HREF)
        try:
           self.chrome.find_element(*self.ATRIBUT_HREF)
           assert True, "Elementul a fost gasit"
        except NoSuchElementException:
            print("Elementul nu este afisat")

### Test 6
## - Lasă goale user și pass
## - Click login
##- Verifică dacă eroarea e displayed
    ### nu da ok
    # def test_check_error_is_displayed(self):
    #     self.chrome.get("https://the-internet.herokuapp.com/login")
    #     self.chrome.find_element(*self.LOGIN_BUTTON).click()
    #     # sleep(3)
    #     actual_error_message = WebDriverWait(chrome, 15).until(EC.presence_of_element_located(*self.ERROR_MESSAGE))
    #     self.assertTrue(actual_error_message.is_displayed(), "eroare invizibila")

