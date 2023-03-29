# Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
# ● Id
# ● Link text
# ● Parțial link text
# ● Name
# ● Tag*
# ● Class name*
# ● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())

chrome = webdriver.Chrome(service=s)
chrome = webdriver.Chrome()

chrome.get("https://www.phptravels.net/")
sleep(2)

#id
chrome.find_element(By.ID,"flights-tab").click()
sleep(2)

# id
chrome.find_element(By.ID,"autocomplete").send_keys("Cluj Napoca")
sleep(1)
chrome.find_element(By.ID,"autocomplete2").send_keys("Zanzibar")
sleep(2)

chrome.quit()