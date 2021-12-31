from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
#drag and drop
source = driver.find_element_by_xpath('//*[@id="box3"]')
destination = driver.find_element_by_xpath('//*[@id="box103"]')

source1 = driver.find_element_by_xpath('//*[@id="box6"]')
destination1 = driver.find_element_by_xpath('//*[@id="box106"]')

act = ActionChains(driver)
act.drag_and_drop(source, destination).perform()
act.drag_and_drop(source1, destination1).perform()