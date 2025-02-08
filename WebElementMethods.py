import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import Urls

driver = webdriver.Chrome()
driver.get(Urls.DEMOWEBSHOP)

# is_selected()
pol = driver.find_element(By.ID, "pollanswers-1")
if pol.is_selected():
    pol.click()

# is_displayed() and is_enabled()
link = driver.find_element(By.XPATH, "//a[@class='ico-login']")
if link.is_displayed():
    if link.is_enabled():
        link.click()

# dimension() and point() [.size, .location]
register_btn = driver.find_element(By.XPATH, "//input[@value='Register']")
print(register_btn.size)
print(register_btn.location)

# get_attribute()
print(register_btn.get_attribute("class"))

# get_property()
print(register_btn.get_property("type"))

# get_css_value()
print(register_btn.value_of_css_property("font-size"))

# text
print(driver.find_element(By.TAG_NAME, "h1").text)

# tag_name
print(register_btn.tag_name)

# send_keys() and clear()
driver.find_element(By.ID, "Email").send_keys("email@example.com")
driver.find_element(By.ID, "Email").clear()

# click()
driver.find_element(By.ID, "RememberMe").click()

# submit()
driver.find_element(By.CLASS_NAME, "button-1").submit()

time.sleep(5)
driver.quit()