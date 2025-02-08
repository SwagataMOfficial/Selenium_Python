import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import Urls


driver = webdriver.Chrome()
driver.get(Urls.DEMOWEBSHOP)

links = driver.find_elements(By.XPATH, "//div[@class='header-links']/ul//a")

time.sleep(2)
for link in links:
    print(link.text + "=>", link.get_attribute('href'))

time.sleep(2)
driver.quit()