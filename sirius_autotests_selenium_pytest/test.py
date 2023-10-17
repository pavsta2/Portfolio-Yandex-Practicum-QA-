from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.get("http://tutorialsninja.com/demo/")
time.sleep(10)