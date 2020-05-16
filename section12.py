# 로그인해서 가져오기
from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

# login info(개발자도구)
login_info = {
    '__RequestVerificationToken': "FCwvkSqyp4o1aV1xnK4ZmhQwu_yJNDjDlyBTjgZg_DJUVoUubFhfv0OEBdIAvf194sFODSb8fGwn_6AbSsZz-YwQQ5VXVUEWTqQWc075tuB06m_pbMlvZ5tr4Rwf5BO-P_K051YcmdX1VI2yW6OmqXynJp_pDdePY9yObz3Wq0s1",
    'command': 'login',
    'valid_url': '',
    'valid_key': '',
    'member_type': 'MEM',
    'type': '',
    'untrustCheck': "? 1 : 0",
    "FailCheck": "0",
    "url": "https%3a%2f%2fwww.gmarket.co.kr%2f",
    "PrmtDisp": '',
    "PrmtreferURL": "https%3a%2f%2fwww.gmarket.co.kr%2f",
    "FromWhere": "G",
    "socialType": '',
    "socialSessionId": '',
    "member_yn": "Y",
    "id": "hsm0156",
    "pwd": "qhfltm23@#",
    "buyer_nm": '',
    "buyer_tel_no1": '',
    "buyer_tel_no2": '',
    "buyer_tel_no3": '',
    "nonmem_passwd": '',
}
# headers
headers = {
    "User-Agent": UserAgent().chrome,
    "Referer": "https://signinssl.gmarket.co.kr/LogOut/LogOut"
}

with requests.Session() as s:
    res = s.post("https://signinssl.gmarket.co.kr/LogIn/LogInProc",
                 login_info, headers=headers)
    print(res.status_code)
    res = s.get("http://gbank.gmarket.co.kr/Home/MyCoupon", headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')
    check_name = soup.select('a')
    print(check_name)
    #시발 왜 로그인 안돼 ㅡㅡ 좆같네
    