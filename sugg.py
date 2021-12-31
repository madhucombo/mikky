import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path=r'C:\Users\kumar\Downloads\chromedriver_win32\chromedriver')
# webdriver.Firefox
driver.get("https://www.google.com/")
driver.maximize_window()

driver.find_element_by_name("q").send_keys("indian cricket team")
time.sleep(3)
sugg = driver.find_elements_by_xpath('//li[@data-view-type="1"]')
print(sugg)
for tag in sugg:
    print(tag.text)