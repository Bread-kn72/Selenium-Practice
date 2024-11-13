from selenium import webdriver
from test_cases.test_case1 import test_case1
from test_cases.test_case2 import test_case2
from test_cases.test_case3 import test_case3

driver = webdriver.Chrome()

try:
    test_case1(driver)
    test_case2(driver, "김민재")
    test_case3(driver)

finally:
    driver.quit()
    print("모든 테스트 완료")
