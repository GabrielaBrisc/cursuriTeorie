from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()

chrome.get("https://formy-project.herokuapp.com/form")
sleep(2)

name = chrome.find_element(By.ID,"first-name")
name.send_keys("Elena")
sleep(2)
name.clear()
sleep(2)

#### TAG NAME
tag_name = chrome.find_element(By.TAG_NAME,"input")
tag_name.send_keys("testttt@@@@")
sleep(3)

list_of_input_elem = chrome.find_elements(By.TAG_NAME, "input")
list_of_input_elem[2].send_keys("QA")
sleep(2)

chrome.quit()