import time
from selenium import webdriver
import Urls

driver = webdriver.Chrome()
driver.get(Urls.GOOGLE)

# Maximize the window
driver.maximize_window()
time.sleep(1)

# Minimize the window
driver.minimize_window()
time.sleep(1)

# Fullscreen the window
driver.fullscreen_window()
time.sleep(1)

# refresh the window
driver.refresh()
time.sleep(1)

# Get the window size
print(driver.get_window_size())
time.sleep(1)

# Set the window size
driver.set_window_size(800, 600)
time.sleep(1)

# Get the window position
print(driver.get_window_position())
time.sleep(1)

# Set the window position
driver.set_window_position(200, 200)
time.sleep(1)

# Get the window handle
print(driver.current_window_handle)
time.sleep(1)

# Get the window handles
print(driver.window_handles)
time.sleep(1)
# Get the window title
print(driver.title)
time.sleep(1)
# Get the window URL
print(driver.current_url)
time.sleep(1)
# Get the window source
# print(driver.page_source)

time.sleep(2)
driver.quit()