from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome  = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")


# selector by XPATH -> atribut=valoare
# chrome.find_element(By.XPATH,"//input[@id='first-name']").send_keys("ABC")

#selector by XPATH -> * (toate elemente care respecta regula data)
# chrome.find_element(By.XPATH,"//*[@id='first-name']").send_keys("ABC2")
#
# #selector by XPATH -> navigare in jos - trecem prin fiecare element
# chrome.find_element(By.XPATH,"//div/div/input[@id='first-name']").send_keys("ABC3")
#
# #selector by XPATH -> navigare in jos - skip tags- cautam oriunde sub form un input care sa respecte regula
# chrome.find_element(By.XPATH,"//form//input[@id='first-name']").send_keys("ABC4")
#
# #selector by XPATH -> selectam elemente din lista - index-ul incepe de la 1
# chrome.find_element(By.XPATH,"(//input[@class='form-control'])[2]").send_keys("ABC5")
#
# #selector by XPATH -> OR primul gasit dintr variabile
# chrome.find_element(By.XPATH,"//input[@id='last-name'] | //input[@id='last-name2']").send_keys("ABC6")
#
# #selector by XPATH -> in functie de textul partial (sau complet) + luam textul de pe el cu propritatea text
# text = chrome.find_element(By.XPATH,"//a[contains(text(),'Formy')]").text
#
# #selector by XPATH -> in functie de textul vizibil
chrome.find_element(By.XPATH,'//a[text()="Submit"]').click()

sleep(5)

