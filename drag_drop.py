from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path=r'C:\Users\kumar\Downloads\chromedriver_win32\chromedriver')

driver.get('file:///C:/Users/kumar/Downloads/drag_drop.html')
time.sleep(10)
act=ActionChains(driver)
object=driver.find_element_by_xpath('//div[@id="draggable"]')
target=driver.find_element_by_xpath('//div[@id="droppable"]')
act.click_and_hold(object)
act.release(target)
act.perform() #without act.perform action won't be performed
print(target.text)
time.sleep(10)
driver.close()
driver.quit()