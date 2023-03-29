from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


chrome  = webdriver.Chrome()
chrome.get("https://www.emag.ro/#opensearch")

# 1.selector by XPATH -> atribut=valoare
chrome.find_element(By.XPATH,"//input[@id='searchboxTrigger']").send_keys("iphone 13 pro")
sleep(3)

# #  1.selector by XPATH -> navigare in jos - trecem prin fiecare element
##click pe search button
chrome.find_element(By.XPATH,"/html/body/div[4]/nav[1]/div/div/div[2]/div/form/div[1]/div[2]/button[2]/i").click()
sleep(3)

# 2.selector by XPATH -> atribut=valoare
#insert apple in brand search field
## aici pune la primul - am nevoie de index

chrome.find_element(By.XPATH,"//input[@class='js-filter-search filter-search-input form-control input-sm']")
# list_search_field[1].send_keys("apple") - nu merge cu lista
sleep(3)

# #selector by XPATH -> navigare in jos - trecem prin fiecare element
# click pe apple de la brand
chrome.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/section[1]/div/div[3]/div[2]/div[5]/div[1]/div/div/div[3]/div/h2/a").click()
sleep(3)

