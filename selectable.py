from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path=r'C:\Users\kumar\Downloads\chromedriver_win32\chromedriver')
driver.get(r"C:\Users\Manosasi\Desktop\html files\selectable.html")
time.sleep(5)
act=ActionChains(driver)
obj1=driver.find_element(By.XPATH,'//li[text()="Item 2"]')
obj2=driver.find_element(By.XPATH,'//li[text()="Item 6"]')

act.click_and_hold(obj1)
act.click_and_hold(obj2)
act.perform()
time.sleep(10)
driver.close()
# driver.quit()