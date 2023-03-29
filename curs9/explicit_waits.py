from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome  = webdriver.Chrome()
chrome.maximize_window()
chrome.get("https://formy-project.herokuapp.com/form")

# selenium va cauta toate elemente timp de 5 secunde
chrome.implicitly_wait(5)

#Explicit wait
#Astepta maxim 15 secunde pentru a gasi elementul cu id-ul "first-name" (in acest caz, elementul este gasit instant, nu am avea nevoie de acest explicit wait)
first_name = WebDriverWait(chrome,15).until(EC.presence_of_element_located((By.ID,"first-name")))
first_name.send_keys("Valentin")

# aici va astepta implicit 5 secunde pentru a gasi elementul (in cazul de fata nu este nevoie deoarece il gaseste instant)
chrome.find_element(By.ID,"last-name").send_keys("Slavescu")

try:
    first_name_2 = WebDriverWait(chrome,15).until(EC.presence_of_element_located((By.ID,"first-name222")))
    first_name.send_keys("Valentin")
except Exception as e:
    print(e)
# sleep(5)


chrome.quit()