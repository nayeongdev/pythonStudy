from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
# 브라우저 꺼짐 방지
options.add_experimental_option("detach", True)
# 불필요한 에러 메세지 삭제
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# browser = webdriver.Chrome()
# create service after automatically setting the lastest version of chromedriver
# service = Service(executable_path=ChromeDriverManager().install())
# browser = webdriver.Chrome(service=service, options=options)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                           options=options)

browser.get("http://naver.com")

loginBtn = browser.find_element(By.CLASS_NAME, "link_login")
loginBtn.click()
browser.back()
browser.forward()
browser.back()
browser.refresh()  # 브라우저 새로고침
search = browser.find_element(By.ID, "query")
search.send_keys("나도 코딩")
search.send_keys(Keys.ENTER)
elem = browser.find_elements(By.TAG_NAME, "a")
for e in elem:
    e.get_attribute("href")   # href 속성값 추출
browser.get("http://daum.net")
search = browser.find_element(By.NAME, "q")
search.send_keys("나도 코딩")
search.send_keys(Keys.ENTER)
browser.back()
search = browser.find_element(By.NAME, "q")
search.send_keys("나도 코딩")
searchBtn = browser.find_element(By.XPATH,
                                 '//*[@id = "daumSearch"]/fieldset/div/div/button[3]')
searchBtn.click()

browser.close()  # 그냥 창 닫기
browser.quit()  # 모두 종료
