import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path=r'C:\Users\kumar\Downloads\chromedriver_win32\chromedriver')

driver.get('https://www.redbus.com/')
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("//input[@id='src']").send_keys("Chennai")
driver.find_element_by_xpath("//input[@id='dest']").send_keys('Bangalore')
driver.find_element_by_xpath("//label[@for='onward_cal']").click()

def select_date():
    driver.find_element_by_xpath("//div[@class='rb-calendar']//td[@class='monthTitle']")
    if month_year=='Jan 2022':
        time.sleep(3)
        driver.find_element_by_xpath("//div[@class='rb-calendar'](//td[@class='wd day'])[20]").click()
    else:
        time.sleep(3)
        driver.find_element_by_xpath(("//div[@class='rb-calendar'](//td[@class=''])[20]").click()
        select_date()
select_date()
