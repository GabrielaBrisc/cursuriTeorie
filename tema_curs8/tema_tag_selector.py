from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")

chrome.find_element(By.TAG_NAME,"input").send_keys("testttt@@@@")
sleep(5)

chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/autocomplete")


list_of_input_elem = chrome.find_elements(By.TAG_NAME, "input")
list_of_input_elem[1].send_keys("test@@@@")
sleep(4)

# chrome.quit()