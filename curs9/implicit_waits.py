from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome  = webdriver.Chrome()
chrome.get("https://formy-project.herokuapp.com/form")

"""
Exemplu: Vrem sa cautam un element cu id-ul first-name pe pagina
Sistemul va cauta acel element, si daca il va gasi, va trece instant la urmatoarea instructiune

Da nu il gaseste, sistemul va continua sa-l caute pe toata duata stabilita de implicit wait
si daca nu il gaseste pana la finalul duratei, va returna eroare

!!!Atentie!!! Daca nu am avea acel implicit wait, atunci va returna eroare instant
"""
#pentru acest elementu nu va astepta 10 secunde
#chrome.find_element(By.ID,"first-name").send_keys("Valentin")

#De aici in jos va astepta 10 secunde pentru fiecare element pe care dorim sa-l gasim.
chrome.implicitly_wait(10)

chrome.find_element(By.ID,"first-name").send_keys("Valentin")

print("Instructiunea urmatoare")

# de aici in jos se va astepta maxim 2 secunde
# chrome.implicitly_wait(2) # suprascriem implicit wait-ul de mai sus

# chrome.find_element(By.ID, "first-name222").send_keys("Nu gasesc")
print("Instructiunea urmatoare 2")

chrome.quit()

"""
Setam implicit wait in secunde:
    - o modalitate prin care definim un timp global de asteptare 
    pana cand sa dea eroarea cand elementul nu a fost gasit
    - se va instantia in momentul in care va fi executata instructiunea implicitly_wait() si va fi distrus in momentul in care executia se incheie si browserul se inchide

Selenium va cauta toate elementele maxim x secunde

Diferenta intre implicit wait si sleep este ca instructiunea de sleep va "astepta" orice ar fi (indiferent daca gaseste elementul sau nu) 
(pune pauza la tot codul indiferent de stadiul sau)
iar implicit wait continua sa caute in acel numar de secunde elementul pana il gaseste. 
"""