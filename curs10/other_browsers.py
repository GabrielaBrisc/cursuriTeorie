from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

# CHROME

# chrome = webdriver.Chrome()
# chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

### FIREFOX
driver = webdriver.Firefox()

driver.maximize_window()
driver.get("https://formy-project.herokuapp.com/form")
driver.find_element(By.ID,"first-name" ).send_keys("TEST")
sleep(3)
driver.quit()

