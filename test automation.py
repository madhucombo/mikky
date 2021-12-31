from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path=r'C:\Users\kumar\Downloads\chromedriver_win32\chromedriver')
driver.get('https://itera-qa.azurewebsites.net/home/automation')
driver.maximize_window()
driver.implicitly_wait(500)

driver.find_element(By.XPATH,'//input[@id="name"]').send_keys("himabindu")
driver.find_element(By.XPATH,'//input[@id="phone"]').send_keys("9703622043")
driver.find_element(By.XPATH,'//input[@id="email"]').send_keys("himabindureddy45@gmail.com")
driver.find_element(By.XPATH,'//input[@id="password"]').send_keys("Bindureddy@45")
driver.find_element(By.XPATH,'//textarea[@id="address"]').send_keys("3/62B,Kottapalli(V),Obulavaripalli(M),Kadapa(Dist.),516108")
#driver.find_element(By.XPATH,'//input[@id="female"]').click()
driver.find_element(By.CSS_SELECTOR,'#female').click()
driver.find_element(By.CSS_SELECTOR,'#monday').click()
driver.find_element(By.XPATH,'//option[@value="3"]').click()
driver.find_element(By.XPATH,'(//label[@class="custom-control-label"])[2]').click()
driver.find_element(By.XPATH,'//label[text()="Selenium Webdriver"]').click()
driver.find_element(By.XPATH,'//label[text()="TestNG"]').click()
s=driver.find_element(By.XPATH,'//input[@class="custom-file-input"]')
#s.send_keys("C://Users//Manosasi//Desktop//sample.png.png")
s.send_keys("C://Users/Manosasi/PycharmProject/webdriver.py")
s.find_element(By.XPATH,'//div[@class="input-group-append"]').click()