from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



#initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

#maximizam fereastra
chrome.maximize_window()

#navigam catre un URL
chrome.get('https://sit.smarty.3.uk/')

