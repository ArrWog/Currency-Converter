import requests
from bs4 import BeautifulSoup
import time

DOLLAR_RUB = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=ljkkfh+&aqs=chrome.2.69i57j0i10i131i433i512l4j0i10i512j0i10i433i512j0i10i512j0i10i131i433i512l2.3426j1j7&sourceid=chrome&ie=UTF-8'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}


def check_currency():
    full_page = requests.get(DOLLAR_RUB, headers=headers)

    soup = BeautifulSoup(full_page.content, 'html.parser')

    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})
    print('сейчас курс 1 доллара = ' + convert[0].text)
    time.sleep(3)
    check_currency()


check_currency()
