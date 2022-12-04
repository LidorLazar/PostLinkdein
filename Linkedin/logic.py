import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def open_web():
    driver = webdriver.Chrome('./chromedriver.exe')
    url = 'https://www.linkedin.com/'
    driver.get(url)

