import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import Urls

driver = webdriver.Chrome()
driver.get(Urls.DEMOWEBSHOP)

# Locator 1 - TAG_NAME
driver.find_element(By.TAG_NAME, 'a').click()
time.sleep(1.5)

# Locator 2 - ID
driver.find_element(By.ID, 'small-searchterms').send_keys('Books')
time.sleep(1.5)

# Locator 3 - NAME
driver.find_element(By.NAME, 'pollanswers-1').click()
time.sleep(1.5)

# Locator 4 - CLASS_NAME
driver.find_element(By.CLASS_NAME, 'search-box-button').click()
time.sleep(1.5)

# Locator 5 - LINK_TEXT
driver.find_element(By.LINK_TEXT, 'Apparel & Shoes').click()
time.sleep(1.5)

# Locator 6 - PARTIAL_LINK_TEXT
driver.find_element(By.PARTIAL_LINK_TEXT, 'Digital down').click()
time.sleep(1.5)

# Locator 7 - CSS_SELECTOR
driver.find_element(By.CSS_SELECTOR, "a[class='ico-register']").click()
time.sleep(1.5)

# Locator 8 - XPATH
driver.find_element(By.XPATH, "//div[@class='form-fields']/div[3]/input").send_keys("Singh")

# Termination
time.sleep(3)
driver.quit()