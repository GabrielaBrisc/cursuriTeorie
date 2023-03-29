from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get("http://www.seleniumframework.com/Practiceform/")

chrome.find_element(By.NAME, "country").send_keys("Romania")
sleep(2)

chrome.quit()