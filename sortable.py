from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome(executable_path=r'C:\Users\kumar\Downloads\chromedriver_win32\chromedriver')
driver.get(r"C:\Users\Manosasi\Desktop\html files\sortable.html")
time.sleep(10)
act=ActionChains(driver)
items=driver.find_elements(By.XPATH,'//*[@id="sortable"]/li')
object=driver.find_element(By.XPATH,'//*[@id="sortable"]/li[1]')
target=driver.find_element(By.XPATH,'//*[@id="sortable"]/li[7]')

act.drag_and_drop(target,object)

act.perform()
time.sleep(10)