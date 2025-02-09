import time
from selenium import webdriver
import Urls

driver = webdriver.Chrome()
driver.get(Urls.DEMOWEBSHOP)
driver.get(Urls.GOOGLE)

time.sleep(2)
# Navigate back
driver.back()
time.sleep(2)

# Navigate forward
driver.forward()
time.sleep(2)

# Refresh the page
driver.refresh()

time.sleep(2)
driver.quit()