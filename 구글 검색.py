from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

def go_to_google():
    driver.get('https://www.google.com')
    time.sleep(2)

def search_keyword(keyword):
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

try:
    go_to_google()
    search_keyword("먼슬리키친")

    go_to_google()
    search_keyword("adb 사용법")

    time.sleep(3)

    time.sleep(10)

finally:
    driver.quit()

