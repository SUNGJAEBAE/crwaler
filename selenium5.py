# 다나와에서 가져와보자 ajax형태다
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests

findingEleNum = 11
count = 1
chrome_options = Options()
# chrome_options.add_argument("--headless")  # 브라우저가 실행안되고 안에서 실행됨
chrome_options.add_argument("--mute-audio")
for count in range(2, 32):
    browser = webdriver.Chrome(
        'C:/tools/webdriver/chromedriver.exe', options=chrome_options)

    browser.implicitly_wait(0.5)

    browser.set_window_size(1200, 800)
    browser.get("https://www.fastcampus.co.kr/courses/200328/clips/")

    element_id = browser.find_element_by_css_selector("#user-email")
    element_password = browser.find_element_by_css_selector("#user-password")

    element_id.send_keys('hsm0156@gmail.com')
    element_password.send_keys('qhfltm23@#')
    element_password.submit()
    # # 다 그려진 다음에 클릭하려고 하는 부분
    WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".fco-confirm-modal__footer__cancel"))).click()

    time.sleep(2)
    try:
        print(browser.find_element_by_css_selector(
            f"div.fco-chapter-list > ul:nth-child({findingEleNum}) .fco-chapter-toggle-list__content"))
        print("aleary tab open")
    except:
        print("no such thing")
        browser.find_element_by_css_selector(
            f"div.fco-chapter-list > ul:nth-child({findingEleNum}) > li > div > div > div > span").click()

    time.sleep(3)
    browser.find_element_by_css_selector(
        f"div.fco-chapter-list > ul:nth-child({findingEleNum}) div.fco-chapter-toggle-list__content li:nth-child({count})").click()

    time.sleep(3)

    try:
        WebDriverWait(browser, 3).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.fco-confirm-modal__header > div > svg"))).click()
    except:
        pass
    time.sleep(1)

    frame = browser.find_elements_by_css_selector("iframe")[0]
    browser.switch_to.frame(frame)
    time.sleep(1)
    ans = browser.find_element_by_css_selector("#kollus_player_html5_api")

    chunk_size = 1024

    url = ans.get_attribute('src')
    r = requests.get(url, stream=True)

    with open(f'hacked{count}.mp4', 'wb') as f:
        for chunk in r.iter_content(chunk_size=chunk_size):
            f.write(chunk)

    browser.close()
