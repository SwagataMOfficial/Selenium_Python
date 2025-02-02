import time
from selenium import webdriver
import Urls

driver = webdriver.Chrome()
driver.get(Urls.GOOGLE)
time.sleep(3)
driver.quit()