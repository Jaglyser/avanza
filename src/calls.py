from requests import post, get, Session
from login import Login as ln
from paths import constants, BASE_URL


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

    def authenticate(self):
        self._authenticationTimeout = 1440

        cookies = self.cookies
        data = {
            'maxInactiveMinutes': self._authenticationTimeout,
            'username': 'jaglyser',
            'password': '4972Njej'
        }

        url = f"{BASE_URL}{constants['paths']['AUTHENTICATION']}"
        response = post(url, data, cookies=self.cookies)
        print(response.json)


calls = Calls()
calls.authenticate()
