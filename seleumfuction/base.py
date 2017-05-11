from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Safari()
try:
    browser.get('http://fgowiki.com/guide')
    input = browser.find_element_by_class_name('form-control guanjian')
    input.send_keys('贞德')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser,10)
    wait.until(EC.presence_of_all_elements_located(By.CLASS_NAME ,'data pull-left'))
    print(browser.current_url)
    print(browser.get_cookie())
    print(browser.page_source)
finally:
    browser.close()