import unittest
from time import sleep

import webdriver_manager.drivers.chrome
from selenium import webdriver
from selenium.webdriver.common.by import By


class Alerts(unittest.TestCase):
    RESULT_MESSAGE = (By.ID,"result")
    ALERT_BUTTON = (By.XPATH,"//button[text()='Click for JS Alert']")
    CONFIRM_BUTTON = (By.XPATH,"//button[text()='Click for JS Confirm']")
    PROMPT_BUTTON = (By.XPATH,"//button[text()='Click for JS Prompt']")


    ###se exe inainte de fiecare test
    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(3)
        self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")

    def tearDown(self):
        self.chrome.quit()

    def test_alert(self):
        ###pt ca e tupla punem *
        self.chrome.find_element(*self.ALERT_BUTTON).click()
        obj = self.chrome.switch_to.alert #ne am mutat de pe pg noastra pe fereastra de alert
        ### si am salvat fereastra de alerta intr o variabila (obj)
        print(f"Mesaj alerta: {obj.text}")
        sleep(5)

        obj.accept() ## aceasta met este echivalentul click ului pe butonul "ok" din alerta
        # sleep(5)
        expected_text = "You successfully clicked an alert"
        actual_text = self.chrome.find_element(*self.RESULT_MESSAGE).text
        self.assertEqual(actual_text, expected_text, "Mesajul nu este cel dorit")

    def test_confirm_ok(self):
        self.chrome.find_element(*self.CONFIRM_BUTTON).click()
        obj = self.chrome.switch_to.alert
        print(f"Mesaj alerta: {obj.text}")
        # sleep(3)
        obj.accept()
        expected_text = "You clicked: Ok"
        actual_text = self.chrome.find_element(*self.RESULT_MESSAGE).text
        self.assertEqual(actual_text, expected_text, "Mesajul nu este cel dorit")

    def test_confirm_cancel(self):
        self.chrome.find_element(*self.CONFIRM_BUTTON).click()
        obj = self.chrome.switch_to.alert
        print(f"Mesaj alerta: {obj.text}")
        # sleep(3)
        obj.dismiss() ## echiv la clikc ul pe butonul de Cancel din Confirm alert
        expected_text = "You clicked: Cancel"
        actual_text = self.chrome.find_element(*self.RESULT_MESSAGE).text
        self.assertEqual(actual_text, expected_text, "Mesajul nu este cel dorit")
    @unittest.skip
    def test_prompt_text_ok(self):
        self.chrome.find_element(*self.PROMPT_BUTTON).click()
        obj = self.chrome.switch_to.alert
        print(f"Mesaj alerta: {obj.text}")
        sleep(3)
        text = "Test1"
        obj.send_keys(text)
        sleep(2)
        obj.accept()
        expected_text = f"You entered: {text}"
        actual_text = self.chrome.find_element(*self.RESULT_MESSAGE).text
        self.assertEqual(actual_text, expected_text, "Mesajul nu este cel dorit")

