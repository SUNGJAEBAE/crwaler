from selenium import webdriver

browser = webdriver.Chrome('C:/tools/webdriver/chromedriver.exe')

# 0.5초 대기
browser.implicitly_wait(0.5)

browser.set_window_size(600, 800)

browser.get('https://naver.com')

#print(f'page contents : {browser.page_source}')

print(f'session Id : {browser.session_id}')
print(f'title : {browser.title}')
print(f'URL : {browser.current_url}')
print(f'cookies :{browser.get_cookies()}')

# 가서 스크린샷을 찍어보자
# 검색창 선택
element = browser.find_element_by_css_selector('#query')
element2 = browser.find_element_by_css_selector('div.logo_area > h1 > a')
element.send_keys('방탄소년단')
print(element.get_attribute("value"))
print(element2.get_attribute('class'))
element.submit()

browser.find_element_by_css_selector("li.lnb4 > a > span").click()

# browser.save_screenshot('./result3/website1.png')

# browser.get_screenshot_as_file("./result3/website2.png")

browser.quit()
