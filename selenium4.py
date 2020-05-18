# 다나와에서 가져와보자 ajax형태다
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import urllib.request as req
import xlsxwriter
from io import BytesIO
chrome_options = Options()
chrome_options.add_argument("--headless")  # 브라우저가 실행안되고 안에서 실행됨

workbook = xlsxwriter.Workbook("./crwaling_result.xlsx")
worksheet = workbook.add_worksheet()
browser = webdriver.Chrome(
    'C:/tools/webdriver/chromedriver.exe', options=chrome_options)

browser.implicitly_wait(0.5)

browser.set_window_size(600, 800)
browser.get("http://prod.danawa.com/list/?cate=112758&15main_11_02")

# 다 그려진 다음에 클릭하려고 하는 부분
WebDriverWait(browser, 3).until(EC.presence_of_element_located((
    By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()

# 무조건 2초 기다리는거. 위에껀 로딩 끝나면 그래도 바로 클릭함.
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="searchMaker1452"]').click()
WebDriverWait(browser, 3).until(EC.presence_of_element_located((
    By.XPATH, '//*[@id="searchMaker1452"]'))).click()

# print('now find', browser.page_source)
cur_page = 1
target_crawl_num = 5
int_cnt = 1
while cur_page <= target_crawl_num:

    print('******current page : {}'.format(cur_page))

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # print(soup.prettify())

    pro_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')
    for v in pro_list:
        if not v.find('div', class_="ad_header"):

            prod_name = (v.select('p.prod_name > a')[0].text.strip())
            # print(v.select('a.thumb_link > img')[0]['data-original'])
            if 'data-original' in v.select('a.thumb_link > img')[0].attrs:
                response = req.urlopen(v.select('a.thumb_link > img')[
                                       0]['data-original'])
                content = response.read()
                img_data = BytesIO(content)
            prod_price = (v.select('p.price_sect >a')[0].text.strip())
            worksheet.write('A%s' % int_cnt, prod_name)
            worksheet.write('B%s' % int_cnt, prod_price)

            int_cnt += 1
        print()
    print()
    browser.save_screenshot(f'./result3/target_page{cur_page}.png')
    cur_page += 1
    WebDriverWait(browser, 3).until(EC.presence_of_element_located((
        By.CSS_SELECTOR, f'.number_wrap > a:nth-child({cur_page})'))).click()

    time.sleep(3)
    del soup
browser.close()
workbook.close()
