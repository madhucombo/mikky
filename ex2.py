from selenium import webdriver
from selenium.webdriver.common.keys import Keys
madhu=webdriver.Chrome(executable_path=r'C:\Users\kumar\Downloads\chromedriver_win32\chromedriver')
madhu.get('https://www.google.co.in/')
madhu.maximize_window()
madhu.find_element_by_name('q').send_keys('India')
madhu.find_element_by_xpath("(//input[@class='gNO89b'])[2]").click()
print(madhu.title)
print(madhu.current_url)
# madhu.execute_script('')
# madhu.find_element_by_xpath('').click()
madhu.back()

