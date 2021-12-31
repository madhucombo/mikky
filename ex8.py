from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time

web = webdriver.Chrome()
web.get("https://itera-qa.azurewebsites.net/home/automation")
web.maximize_window()
time.sleep(2)
"""
1.how many boxes were present in page
2.how to provide value into input boxes
3.how to get the status of text boxes
"""

# boxes = web.find_elements(By.CLASS_NAME, 'form-control')
# print(len(boxes))   # this gives the number of boxes present in page
name = web.find_element(By.XPATH, '//input[@id ="name"]')
name.send_keys("Anudeep")
time.sleep(2)
print(name.is_displayed())    # used to
time.sleep(2)

number = web.find_element(By.ID, 'phone')
time.sleep(2)
number.send_keys('9966353664')                  # to enter the value use send keys
time.sleep(2)

mail = web.find_element(By.ID, 'email')
time.sleep(2)
mail.send_keys('deep.sam.479@gmail.com')
time.sleep(2)

pw = web.find_element(By.ID, 'password')
time.sleep(2)
pw.send_keys('Anudeep@123')
time.sleep(2)

add = web.find_element(By.ID, 'address')
time.sleep(2)
add.send_keys('Qtr No A2/6, Vizag')
time.sleep(2)

'''
we will work on Radio buttons..
1. it is selected or not by isSelected()
2. clicking the button using 'click()'
'''

r_buttons = web.find_element(By.XPATH, '((//input[@type="radio"])[2])')
print(r_buttons.is_selected())     # returns whether the radio is clicked or not
time.sleep(2)
r_buttons.click()

# c_boxes = web.find_elements(By.XPATH, '//class[@id="form-check-input"]')
# print(len(c_boxes))
day_1 = web.find_element(By.ID, 'friday')
day_2 = web.find_element(By.ID, 'saturday')
day_3 = web.find_element(By.ID, 'sunday')
day_1.click()
time.sleep(2)
day_2.click()
time.sleep(2)
day_3.click()
time.sleep(2)
day_1.is_selected()
day_2.is_selected()
day_3.is_selected()             #retruns the boolean as true for selected & false for not selected

'''
working on dropdowns 
1. we can select only one option
2. we can even find out number of options available
3. we have 3 ways to select the options
    i.  select_by_index
    ii. select_by_value
    iii.select_by_visible_text
'''
drop = Select(web.find_element(By.CLASS_NAME, 'custom-select'))
drop.select_by_visible_text('Italy')
time.sleep(2)
# drop.select_by_index(3)
# drop.select_by_value('7')

print(len(drop.options))  # this will give the number of options available
countries = drop.options
for country in countries:
    print(country.text)          # this will print every text present in it.

web.find_element(By.XPATH, '//*[@for="3years"]').click()

'''
this will select the check boxes in the selected courses
frameworks and etc
'''
web.find_element(By.XPATH, '(//label[@class="custom-control-label"])[6]').click()
web.find_element(By.XPATH, '(//label[@class="custom-control-label"])[9]').click()
web.find_element(By.XPATH, '(//label[@class="custom-control-label"])[8]').click()

# upload a file
file = web.find_element(By.XPATH, '//input[@id="inputGroupFile02"]')
file.send_keys('C:\\Users\\ANUDEEP\\Pictures\\nature.jpg')
web.find_element(By.CLASS_NAME, 'input-group-append').click()