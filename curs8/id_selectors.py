from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

"""
ex de elem html: <input type="text" class="form-control" id="first-name" placeholder="Enter first name">
id = atribut
first-name = valoarea atributului 
"""
### initializam chrome
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)

###incepand cu 4.6.0 nu mai este nevoie sa facem setarile de la liniile de mai sus
chrome = webdriver.Chrome()

chrome.get("https://formy-project.herokuapp.com/form") ##met get este o met prin care putem naviga la un anumit link


sleep(3) ###met prin care punem pauza codului sa nu mai faca nimic timp de 3 sec inainte de a se exe restul instructiunilor

###<input type="text" class="form-control" id="first-name" placeholder="Enter first name">
name = chrome.find_element(By.ID,"first-name")

#met send_keys este met pe care o fol sa transmitem text intr un camp din pg
name.send_keys("ELena")
sleep(4)

###met in lant (chaining)
chrome.find_element(By.ID,"last-name").send_keys("Popescu")
sleep(2)
name.clear()
sleep(4)
chrome.quit() ###met fol pt a inchide browserul, implicit si tab urile
# chrome.close() ###met care inchide tab-ul curent


#####  LINK TEXT