from test_cases.test_case1 import test_case1, driver
from test_cases.test_case2 import test_case2

try:
    test_case1()
    test_case2(driver, "김민재")

finally:
    driver.quit()
    print("모든 테스트 완료")
