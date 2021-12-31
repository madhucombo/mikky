from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(3)
double_click = driver.find_element_by_xpath('//*[@id="HTML10"]/div[1]/button')

time.sleep(3)
act = ActionChains(driver)
act.double_click(double_click).perform()