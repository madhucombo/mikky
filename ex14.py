from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome(executable_path=r'C:\Users\kumar\Downloads\chromedriver_win32\chromedriver')
driver.get('https://testautomationpractice.blogspot.com/?m=1')
driver.maximize_window()

windows=driver.find_element_by_xpath('//input[@class='wikipedia-search-input']').send_keys('Windows')