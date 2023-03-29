from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")

chrome.find_element(By.CSS_SELECTOR,"input#first-name").send_keys("Ionescu")

sleep(2)

###selector by css - atribut=valoare
### [] = indentificator pt atribut = valoare
chrome.find_element(By.CSS_SELECTOR, "input[value='radio-button-1']").click()
sleep(2)

chrome.quit()