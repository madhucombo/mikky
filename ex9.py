from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome(executable_path=r'C:\Users\kumar\Downloads\chromedriver_win32\chromedriver')
driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath("//input[@id='name']").send_keys('Madhumitha')
time.sleep(2)

driver.find_element(By.ID,'phone').send_keys('8667230164')
time.sleep(2)

driver.find_element(By.ID,'email').send_keys('madhumikky1997@gmail.com')
time.sleep(2)

driver.find_element(By.ID,'password').send_keys('8667230164')
time.sleep(2)

driver.find_element(By.ID,'address').send_keys('1/1, Vedagiri Street, Chintadripet')
time.sleep(2)

# driver.find_element_by_xpath("//button[@name='submit']").click()

# Radio buttons
radio=driver.find_element_by_xpath("(//input[@type='radio'])[1]")
radio.click()

day1=driver.find_element(By.ID,'friday')
day1.click()
time.sleep(2)
day2=driver.find_element(By.ID,'saturday')
day2.click()
time.sleep(2)
day3=driver.find_element(By.ID,'sunday')
day3.click()
time.sleep(2)

# dropdowns
dropdown=Select(driver.find_element(By.CLASS_NAME,'custom-select'))
dropdown.select_by_visible_text('Spain')
time.sleep(2)

driver.find_element_by_xpath("(//label[@class='custom-control-label'])[4]").click()
time.sleep(2)

driver.find_element_by_xpath("(//label[@class='custom-control-label'])[6]").click()
time.sleep(2)

driver.find_element_by_xpath("//input[@class='custom-file-input']").click()

# upload a file
file=driver.find_element(By.XPATH,"//input[@class='custom-file-input']")
file.send_keys('C:\\Users\\kumar\\OneDrive\\Pictures\\Screenshots\\Screenshot (17)\\.png')
driver.find_element(By.CLASS_NAME,'input-group-text').click()