from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_case2(driver, search_keyword):
    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys(search_keyword)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)
    print(f"Test case 2 완료")