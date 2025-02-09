import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import Urls

driver = webdriver.Chrome()
driver.get(Urls.DEMOQA + "select-menu")

# Creating an object of Select class and passing address of the dropdown
dropdown = Select(driver.find_element(By.ID, "cars"))

# Selecting the dropdown by index
dropdown.select_by_index(1)
time.sleep(1.5)

# Selecting the dropdown by value
dropdown.select_by_value("opel")
time.sleep(1.5)

# Selecting the dropdown by visible text
dropdown.select_by_visible_text("Audi")
time.sleep(1.5)

# Getting the selected option
# selected_option = dropdown.first_selected_option
# print("Selected option: " + selected_option.text)

# Getting all the options
# all_options = dropdown.options
# print("All options:", all_options)

# deselecting all the options
# dropdown.deselect_all()

# deselecting the option by index
dropdown.deselect_by_index(1)

# deselecting the option by value
dropdown.deselect_by_value("opel")

# deselecting the option by visible text
dropdown.deselect_by_visible_text("Audi")

# Getting all the selected options
# all_selected_options = dropdown.all_selected_options

# Printing all the selected options
# print("All selected options:" , all_selected_options)

# checking if the dropdown is multiple select
is_multiple = dropdown.is_multiple
print("Is multiple:" , is_multiple)

# getting the wrapped element
# wrapped_element = dropdown.wrapped_element
# print("Wrapped element:" + wrapped_element)

time.sleep(2)
driver.quit()