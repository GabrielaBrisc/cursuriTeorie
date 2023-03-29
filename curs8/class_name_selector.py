from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")

###gaseste primul elem si scrie in el
chrome.find_element(By.CLASS_NAME,"form-control").send_keys("Vasile")

list_form_control = chrome.find_elements(By.CLASS_NAME,"form-control")
list_form_control[1].send_keys("Vlad")

#prin clasa select selectam o optiune dintr un dropdown prin textul vizibil de pe site al optiunii
Select(chrome.find_elements(By.CLASS_NAME,"form-control")[3]).select_by_visible_text("5-9")
sleep(3)
Select(chrome.find_elements(By.CLASS_NAME,"form-control")[3]).select_by_index(1)
sleep(3)
Select(chrome.find_elements(By.CLASS_NAME,"form-control")[3]).select_by_value(1)
sleep(5)

chrome.quit()