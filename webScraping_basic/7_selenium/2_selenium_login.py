from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                           options=options)

# 1. naver 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
loginBtn = browser.find_element(By.CLASS_NAME,"link_login")
loginBtn.click()

# 3. id, pw 입력
browser.find_element(By.ID,"id").send_keys("naver_id")
browser.find_element(By.ID,"pw").send_keys("naver_pw")

# 4. login 버튼 클릭
browser.find_element(By.ID, "log.login").click()

# 5. id 새로 입력
# browser.find_element(By.ID,"id").send_keys("my_id") # naver_idmy_id
browser.find_element(By.ID,"id").clear()
browser.find_element(By.ID,"id").send_keys("my_id") # my_id

# 6. html 정보 출력
print(browser.page_source)

# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료
browser.quit()  # 전체 브라우저 종료