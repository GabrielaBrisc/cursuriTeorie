"""
Selectia elem in pagina cu linkText identifica hyperlink-urile din HTML
Textul pe care il dam noi in cod trebuie sa se potriveasca cu textul de la <a> fol in codul HTML
ex: <a class="btn btn-lg" href="/form">Autocomplete</a>
a = def un elem de tip ancora (link catre alta pg)
href = link ul catre care se navigheaza
https://formy-project.herokuapp.com/autocomplete - link complet
/autocomplete - extensia
https://formy-project.herokuapp.com - domeniul
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/")
sleep(2)

chrome.find_element(By.LINK_TEXT,"Autocomplete").click()
sleep(3)
#
# chrome.find_element(By.ID,"logo").click()
# sleep(1)

###verif ca in cazul in care nu se gaseste elem de autocomplete sa nu se opreasca codul de executat
try:
    chrome.find_element(By.LINK_TEXT, "Autocomplete").click()
except:
    print("nu s a gasit elem")
sleep(1)
chrome.quit()

