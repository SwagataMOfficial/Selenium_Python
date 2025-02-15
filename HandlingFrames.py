import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import Urls

driver = webdriver.Chrome()
driver.get(Urls.DEMOAPPS + "ui/frames/nestedWithMultiple?sublist=3")
driver.maximize_window()
time.sleep(5)

driver.switch_to.frame(0)

id_pass = driver.find_elements(By.XPATH, "//p[@class='para']")
un = id_pass[0].text
passwd = id_pass[1].text

# form frame
driver.switch_to.frame(0)

# email textfield frame
driver.switch_to.frame(0)
driver.find_element(By.ID, "email").send_keys(un)

# password textfield frame
driver.switch_to.parent_frame()
driver.switch_to.frame(1)
driver.find_element(By.ID, "password").send_keys(passwd)

# confirm password textfield frame
driver.switch_to.parent_frame()
driver.switch_to.frame(2)
driver.find_element(By.ID, "confirm").send_keys(passwd)

# submit button frame
driver.switch_to.parent_frame()
driver.switch_to.frame(3)
driver.find_element(By.ID, "submitButton").click()

# confirmation checking
driver.switch_to.default_content()
if driver.find_element(By.XPATH, "//div[.='Login successful!']").is_displayed():
    print("Login successful")
else:
    print("Login failed")

time.sleep(5)
driver.quit()