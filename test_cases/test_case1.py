from selenium import webdriver
import time

driver = webdriver.Chrome()

def test_case1():
    driver.get("https://www.google.com")
    time.sleep(2)
    print("test case1 완료")