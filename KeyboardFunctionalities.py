from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

import Urls

driver = webdriver.Chrome()
driver.get(Urls.DEMOWEBSHOP)

driver.find_element(By.XPATH, "//a[@class='ico-register']").click()

input1 = driver.find_element(By.XPATH, '//div[@class="form-fields"]/div[2]//input')
input2 = driver.find_element(By.XPATH, '//div[@class="form-fields"]/div[3]//input')
input3 = driver.find_element(By.XPATH, '//div[@class="form-fields"]/div[4]//input')

input1.send_keys("First value")
input2.send_keys("Second value")

time.sleep(1.5)
input1.send_keys(Keys.CONTROL + 'ax')
input3.send_keys(Keys.CONTROL + 'v')

time.sleep(1.5)
input2.send_keys(Keys.CONTROL + 'ax')
input1.send_keys(Keys.CONTROL + 'v')

time.sleep(1.5)
input3.send_keys(Keys.CONTROL + 'ax')
input2.send_keys(Keys.CONTROL + 'v')

time.sleep(2)
driver.quit()