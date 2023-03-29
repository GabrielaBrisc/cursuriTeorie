"""
Face acelasi lucru ca si LINK_TEXT doar ca va cauta partial nu tot numele link ului

"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/")
sleep(2)
chrome.find_element(By.PARTIAL_LINK_TEXT,"Enabled").click()
sleep(1)
chrome.find_element(By.ID,"logo").click()
sleep(1)
chrome.find_element(By.PARTIAL_LINK_TEXT,"Auto").click()
sleep(2)
chrome.quit()