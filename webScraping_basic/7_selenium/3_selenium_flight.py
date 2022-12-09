import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_util(xpath_str):
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, xpath_str)))


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                           options=options)
browser.maximize_window()
# 1. 네이버 항공권 이동
browser.get("https://flight.naver.com/")

# // <- HTML 전체에서 찾겠다
# button 요소인데 text값이 ""인 것을 찾겠다
begin_date = browser.find_element(By.XPATH, '//button[text()="가는 날"]')
begin_date.click()

# time.sleep(1) # 로딩때문에 1초 대기
WebDriverWait(browser, 30).until(
    EC.presence_of_element_located((By.XPATH, '//b[text()="27"]')))
day27 = browser.find_elements(By.XPATH, '//b[text()="27"]')
day27[0].click()

day31 = browser.find_elements(By.XPATH, '//b[text()="31"]')
day31[0].click()

arrival = browser.find_element(By.XPATH, '//b[text()="도착"]')
arrival.click()

wait_util('//button[text()="국내"]')  # 나올때까지 30초 대기
domestic = browser.find_element(By.XPATH, '//button[text()="국내"]')
domestic.click()

# i태그인데 text가 제주국제공항을 포함하는 것을 찾아줌
jeju = browser.find_element(By.XPATH, '//i[contains(text(),"제주국제공항")]')
jeju.click()

searchBtn = browser.find_element(By.XPATH, '//span[contains(text(),"항공권 검색")]')
searchBtn.click()

# 해당 element가 나타날때(최대 30초)까지 기다림
# 클래스 비교하기위해 @ 붙임
elem = WebDriverWait(browser, 30).until(EC.presence_of_element_located(
    (By.XPATH, '//div[@class="domestic_Flight__sK0eA result"]')))
print(elem.text)

input("종료하려면 enter를 누르세요")
browser.quit()