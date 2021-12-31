from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://swisnl.github.io/jQuery-contextMenu/demo.html')
driver.maximize_window()

time.sleep(3)
right_click = driver.find_element_by_xpath('/html/body/div/section/div/div/div/p/span')

time.sleep(3)
act = ActionChains(driver)
act.context_click(right_click).perform()