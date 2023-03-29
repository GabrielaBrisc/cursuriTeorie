from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")
chrome.find_element(By.TAG_NAME,"input").send_keys("testttt@@@@")
sleep(3)

list_of_input_elem = chrome.find_elements(By.TAG_NAME, "input")
list_of_input_elem[2].send_keys("test@@@@")
sleep(2)
chrome.quit()