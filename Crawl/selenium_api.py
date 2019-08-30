from selenium import webdriver
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver = webdriver.Chrome()
creat_button = driver.find_element_by_xpath()
if creat_button.is_displayed(): #判断是否可见
    pass



#操作下拉菜单
select = selenium.Select(driver.find_element_by_xpath())
s = select.options
select.select_by_visible_text()


#操作alert
alert = driver.switch_to_alert()
alert.accept()

#等待
WebDriverWait(driver,10).untill(lambda s: s.find_element_by_id('').get_attribute('')=='3')
account = WebDriverWait(driver,10).until(expected_conditions.visibility_of_all_elements_located((By.LINK_TEXT,'acount')))
account.click()

#条件设置
account = WebDriverWait(driver,10).until(expected_conditions.element_to_be_clickable((By.NAME,'')))
account = WebDriverWait(driver,10).until(expected_conditions.text_to_be_present_in_element((By.ID,'select-language'),'english'))