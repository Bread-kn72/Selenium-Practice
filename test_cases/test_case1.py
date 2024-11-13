import time

def test_case1(driver):
    driver.get("https://www.google.com")
    time.sleep(2)
    print("test case1 완료")