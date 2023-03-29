from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get("https://auth.emag.ro/user/login")
sleep(2)
### ID
chrome.find_element(By.CSS_SELECTOR,"input[id='user_login_email']").send_keys("brisc.gabriela5@yahoo.com")
sleep(2)
###clasa
chrome.find_element(By.CSS_SELECTOR,"button[class='btn-primary btn']").click()
sleep(15)
# valoare partiala ??
###cu input[type="text"] nu a mers
chrome.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys("Gabtriela Brisc")
sleep(2)