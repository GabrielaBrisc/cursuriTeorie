from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get("https://www.techlistic.com/p/selenium-practice-form.html")
sleep(15)

chrome.find_element(By.LINK_TEXT,"Automate GoDaddy website features with Selenium").click()
sleep(7)

chrome.find_element(By.LINK_TEXT,"Selenium Webdriver Browser Commands").click()
sleep(10)

chrome.find_element(By.LINK_TEXT,"Top 7 Web Development Trends").click()
sleep(5)

### dau scroll down ca sa nu imi dea eroare



########   Parțial link text

chrome.find_element(By.PARTIAL_LINK_TEXT,"Hire WordPress").click()
sleep(4)

chrome.find_element(By.PARTIAL_LINK_TEXT,"DEVELOPERS").click()
sleep(3)

chrome.find_element(By.PARTIAL_LINK_TEXT,"CONTACT").click() #contact us
sleep(3)
# chrome.find_element(By.LINK_TEXT,"Automate Amazon like E-Commerce website with Selenium").click()
# sleep(2)
chrome.quit()