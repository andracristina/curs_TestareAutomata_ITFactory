from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# selector by CSS - ID
chrome.find_element(By.CSS_SELECTOR, 'input#first-name').send_keys('An')

chrome.find_element(By.CSS_SELECTOR, '#job-title').send_keys('tester')

job_title = chrome.find_element(By.CSS_SELECTOR, '#job-title')
job_title.send_keys('tester')

# selector by CSS Class (only the 1st in multiple matches)
chrome.find_element(By.CSS_SELECTOR, 'input.form-control').send_keys('dra')

# selector by CSS atribut = valoare (placeholder)
chrome.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter last name"]').send_keys('Tr')

chrome.find_element(By.CSS_SELECTOR, '[placeholder*="yyyy"]').send_keys('12/03/1234')  # * se pune pt PARTIAL placeholder


job_title.send_keys('QA Engineer')

# selector by CSS atribut = valoare partiala si parinte > copil
chrome.find_element(By.CSS_SELECTOR, 'div input[placeholder*="Enter last name"]').send_keys('ifu')

sleep(3)
chrome.quit()