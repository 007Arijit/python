from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()

driver.get('https://www.motorbazee.com/')
driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div[1]/div/div/ul/li[1]/a').click()
State = driver.find_element(By.ID, "SerchStateBlogTruck")
Drop_Down = Select(State)
#
 # Select Your State
Drop_Down.select_by_visible_text(input("Select your State: "))

time.sleep(3)

City = driver.find_element(By.ID, "SerchCityBlogTruck")
Drop_Down = Select(City)

# Select Your City
Drop_Down.select_by_visible_text(input("Select Your City:  "))

time.sleep(3)

Company = driver.find_element(By.ID, 'SerchMakeBlogTruck')
Drop_Down = Select(Company)

# select Your Car Company
Drop_Down.select_by_visible_text(input('Select Vechile: '))

time.sleep(3)

Model = driver.find_element(By.ID, "SerchModelBlogTruck")
Drop_Down = Select(Model)

# Select Your Model
Drop_Down.select_by_visible_text(input('Select Vehicle Model: '))
#
driver.find_element(By.XPATH, '//*[@id="UsedTruckSubmit"]').click()


