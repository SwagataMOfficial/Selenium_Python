import time
from selenium import webdriver
import Urls

driver = webdriver.Chrome()
driver.get(Urls.DEMOWEBSHOP)

# title
print(driver.title)

# current_url
print(driver.current_url)

# page_source
# print(driver.page_source)

# get_cookies
print(driver.get_cookies())

# delete_all_cookies
driver.delete_all_cookies()
print(driver.get_cookies())


time.sleep(2)
driver.quit()