import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import Urls


driver = webdriver.Chrome()
driver.get(Urls.FACEBOOK)

driver.find_element(By.ID, "email").send_keys("demo@test.com")
driver.find_element(By.ID, "pass").send_keys("password")

driver.find_element(By.NAME, "login").click()

time.sleep(5)
driver.quit()