from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
    
try:
    # 사장님 사이트 진입
    driver.get('https://ceo.monki.net/users/login')
    time.sleep(2)

    #유저타입 선택
    dropdown = Select(driver.find_element(By.ID, "user_type"))
    dropdown.select_by_value("type_003")
    driver.find_element(By.TAG_NAME, "body").click()
    time.sleep(2)
    
    #아이디 입력
    id = driver.find_element(By.ID, "user_id")
    id.clear()
    id.send_keys("monkistore1" + Keys.TAB)
    time.sleep(1)

    #비밀번호 입력
    password = driver.find_element(By.ID, "user_pass")
    password.clear()
    password.send_keys("test123!")

    #자동 로그인 상태 체크
    auto_login = driver.find_element(By.ID, "chkRemember")

    if not auto_login.is_selected():
        auto_login.click()

    #로그인 시도
    time.sleep(1)
    driver.find_element(By.ID, "btnLogin").click()

    time.sleep(10)

finally:
    driver.quit()

