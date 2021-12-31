from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

admin = driver.find_element_by_xpath("//*[@id='menu_admin_viewAdminModule']/b")
user_management = driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
users = driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')

act = ActionChains(driver)
act.move_to_element(admin).move_to_element(user_management).move_to_element(users).click().perform()