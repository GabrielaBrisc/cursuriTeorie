from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome  = webdriver.Chrome()
chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com")


chrome.find_element(By.LINK_TEXT,"Autocomplete").click()

expected_url = "https://formy-project.herokuapp.com/autocomplete2"

# cu .current_url  luam url-ul actual din browser
actual_url = chrome.current_url

assert actual_url == expected_url, f"Invalid url: expected {expected_url} but found {actual_url}"

print("Executia continua")

chrome.quit()