from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
chrome  = webdriver.Chrome()
chrome.get("https://auth.emag.ro/user/login")
sleep(2)

chrome.find_element(By.CLASS_NAME,"form-control").send_keys("brisc.gabriela5@yahoo.com")
sleep(2)
chrome.find_element(By.ID,"user_login_continue").click()
sleep(15)
# chrome.find_element(By.ID,"user_register_full_name").send_keys("Gabriela Brisc")
# sleep(3)
###de ce nu gaseste daca am asa (pt nume si prenume) :
# chrome.find_element(By.CLASS_NAME,"form-control").send_keys("Gabriela Brisc")

list_form_control = chrome.find_elements(By.CLASS_NAME,"form-control")
list_form_control[1].send_keys("Gabriela Brisc")
list_form_control[2].send_keys("ParolaMea123*")
list_form_control[3].send_keys("ParolaMea123*")
sleep(2)

# list_form_control = chrome.find_elements(By.CLASS_NAME,"control-group")
# list_form_control[1].send_keys("Vlad")
# sleep(4)

#prin clasa select selectam o optiune dintr un dropdown prin textul vizibil de pe site al optiunii
# Select(chrome.find_elements(By.CLASS_NAME,"form-control")[3]).select_by_visible_text("5-9")
# sleep(3)
# Select(chrome.find_elements(By.CLASS_NAME,"form-control")[3]).select_by_index(1)
# sleep(3)
# Select(chrome.find_elements(By.CLASS_NAME,"form-control")[3]).select_by_value(1)
# sleep(5)

chrome.quit()