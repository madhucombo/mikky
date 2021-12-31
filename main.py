from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
anu=webdriver.Chrome(executable_path=r'C:\Users\kumar\Downloads\chromedriver_win32\chromedriver')
anu.get("https://www.facebook.com/")
anu.maximize_window()
time.sleep(3)
anu.find_element_by_xpath('//a[@class="_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy"]').click()
time.sleep(3)
anu.find_element_by_name('firstname').send_keys('Madhu')
time.sleep(3)
anu.find_element_by_name('lastname').send_keys('mitha')
time.sleep(3)
anu.find_element_by_name('reg_email__').send_keys('8667230164')
time.sleep(3)
anu.find_element_by_name('reg_passwd__').send_keys('madhu@123')
time.sleep(3)
anu.find_element_by_name('birthday_day').send_keys('20')
time.sleep(3)
anu.find_element_by_id('month').send_keys('May')
time.sleep(3)
anu.find_element_by_id('year').send_keys('1997')
time.sleep(3)
anu.find_element_by_name('sex').click()


