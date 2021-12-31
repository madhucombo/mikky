from selenium import webdriver
import time
from selenium.webdriver.support.select import Select #for dropdown (datepicker)
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path=r'C:\Users\kumar\Downloads\chromedriver_win32\chromedriver')
driver.get('https://wwww.facebook.com/')
driver.maximize_window()
driver.implicitly_wait(10)

# time.sleep(5)
# driver.find_element_by_xpath('(//a[@role="button"])[2]').click()

driver.find_element(By.XPATH,'(//a[@role="button"])[2]').click()
# time.sleep(3)
driver.find_element(By.NAME,'firstname').send_keys('Maddy')
driver.find_element(By.NAME,'lastname').send_keys('micky')
driver.find_element(By.NAME,'reg_email__').send_keys('9944166013')
driver.find_element(By.NAME,'reg_passwd__').send_keys('maddy@123')

# time.sleep(3)
select_day=Select(driver.find_element(By.NAME,'birthday_day'))
# select_day.select_by_index(19)
select_day.select_by_visible_text('20')
# time.sleep(3)
select_month=Select(driver.find_element(By.NAME,'birthday_month'))
select_month.select_by_index(4)
# time.sleep(3)
select_year=Select(driver.find_element(By.NAME,'birthday_year'))
# print(select_year.options)
select_year.select_by_value('1997')
# time.sleep(3)
# select_year.select_by_visible_text('1997')
# time.sleep(3)
driver.find_element(By.XPATH,'(//input[@class="_8esa"])[1]').click()