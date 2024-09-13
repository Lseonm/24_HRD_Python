from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

# ChromeDriver 경로를 Service 객체를 사용하여 설정
chrome_service = Service(r'C:\Program Files\chromedriver-win64\chromedriver-win64\chromedriver.exe')


# WebDriver 객체 생성
driver = webdriver.Chrome(service=chrome_service)




# 현대
for month in range(1, 9):
    hyundai_url = f"https://auto.danawa.com/auto/?Work=record&Tab=Grand&Brand=303&Month=2024-0{month}-00&MonthTo="
    driver.get(hyundai_url)  # 페이지를 브라우저에서 엽니다.

    time.sleep(2)  # 페이지가 로드될 시간을 주기 위해 잠시 대기





# 기아
for month in range(1, 9):
    kia_url = f"https://auto.danawa.com/auto/?Work=record&Tab=Grand&Brand=307&Month=2024-0{month}-00&MonthTo="
    driver.get(kia_url)  # 페이지를 브라우저에서 엽니다.

    time.sleep(2)  # 페이지가 로드될 시간을 주기 위해 잠시 대기








    # # BeautifulSoup을 사용해 HTML 파싱
    # soup = BeautifulSoup(driver.page_source, 'html.parser')
    # tag_t_body = soup.find("tbody")
    #
    # # 크롤링 데이터 저장 리스트
    # Hollys_stores = []
    #
    # for store in tag_t_body.find_all('tr'):
    #     store_td = store.find_all("td")
    #     if len(store_td) >= 6:
    #         store_name = store_td[1].text
    #         store_sido = store_td[0].text
    #         store_address = store_td[3].text
    #         store_phone = store_td[5].text
    #
    #         Hollys_stores.append([store_name, store_sido, store_address, store_phone])
    #
    # # 크롤링 결과 확인
    # print(f"현대 {month}월 판매 실적 : {Hollys_stores}")

driver.quit()  # 브라우저 닫기
