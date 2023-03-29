from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome  = webdriver.Chrome()
chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
sleep(2)

chrome.find_element(By.NAME,"firstname").send_keys("Elena")
sleep(4)
chrome.find_element(By.NAME,"lastname").send_keys("Pop")
sleep(4)
chrome.find_element(By.NAME,"exp").click()
sleep(4)

chrome.quit()