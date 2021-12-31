import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path=r'C:\Users\kumar\Downloads\chromedriver_win32\chromedriver')

driver.get("file:///X:/Selenium%20imp/13.slider.html")
# driver.maximize_window()

slider = driver.find_element(By.XPATH, '//input[@class="slider"]')
act = ActionChains(driver)
time.sleep(10)

act.click_and_hold(slider).move_by_offset(100,0).release().perform()
time.sleep(10)
print(slider.get_attribute('value'))

