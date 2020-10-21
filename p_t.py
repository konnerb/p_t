import requests
import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from bs4 import BeautifulSoup

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "bin/chromedriver")

driver = webdriver.Chrome(executable_path = DRIVER_BIN)


print('**** Running p_t... ****')
driver.get('https://www.metro.ca/en/flyer')
print(driver.title)
time.sleep(8)

try: 
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME , "tbody"))
    )
    print(element)
finally:
    driver.quit()

driver.quit()
print('**** Finished Running p_t ****')