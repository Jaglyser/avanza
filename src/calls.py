from requests import get, Session
from src.login import Login as ln
from src.paths import constants, BASE_URL


class Calls:
    def __init__(self):
        self.cookies = ln.getCookie()

    def getOrderFlow(self, stock):
        url = 'https://www.avanza.se/aktier/nya-dagens-avslut.html/{}'.format(
            stock)
        cookies = self.cookies
        get(url, cookies=cookies)

    def getStockInfo(self, stock):
        cookies = self.cookies
        url = f"{BASE_URL}{constants['paths']['search']}"
        response = get(url, cookies=cookies).json()
        return response

    def getPositions(self):
        cookies = self.cookies
        url = f"{BASE_URL}{constants['paths']['POSITIONS_PATH']}"
        response = get(url, cookies=cookies).json()
        return response
