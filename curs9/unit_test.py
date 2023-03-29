import unittest   #importam libraria unitest care va face programul in bugati rulabile individual
from time import sleep
from unittest import TestCase

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class Test(TestCase):

    # In loc sa repetam elementele in fiecare test, le trecem aici o singura data si dupa le refolosim
    FORM_LINK = (By.LINK_TEXT,"Form")
    SUBMIT_BUTTON = (By.XPATH,"//a[@role='button']")
    JOB_TITLE = (By.ID,"job-title")

    # se ruleaza inainte de fiecare test si are rolul de a face setup pt teste
    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://formy-project.herokuapp.com/")
        # * tuple unpacking -  se ia valoarea din tuple si se da ca argument functiei
        self.chrome.find_element(By.LINK_TEXT,"Form").click()
        # Daca nu facem unpack functia ar arata asa find_element((By.LINK_TEXT,"Form"))
        # Daca facem unpack functia ar arata asa fin_element(By.LINK_TEXT,"Form")

    def tearDown(self):
        self.chrome.quit()

    #Numele medodelor de test trebuie OBLIGATORIU sa inceapa cu test
    def test_url(self):
        actual_url = self.chrome.current_url
        expected_url = "https://formy-project.herokuapp.com/form"
        assert actual_url == expected_url, f"Invalid URL."

    def test_page_title(self):
        actual_title = self.chrome.title
        expected_title = "Formy"
        assert actual_title == expected_title, f"Invalid Title"
        sleep(5)

    # varianta incorecta de a verifica daca nu element nu este afisat
    @unittest.skip   # este un decorator care instruieste sistemul sa sara peste testul respectiv
    def test_element_not_displayed_v1(self):
        self.chrome.get("https://formy-project.herokuapp.com/")
        element = self.chrome.find_element(*self.JOB_TITLE)
        self.assertFalse(element.is_displayed(), "Elementul nu a fost afisat")

    #varianta corecta
    def test_element_not_displayed_v2(self):
        self.chrome.get("https://formy-project.herokuapp.com/")
        try:
           self.chrome.find_element(*self.JOB_TITLE)
           assert False, "Elementul a fost gasit"
        except NoSuchElementException:
            print("Elementul nu este afisat")