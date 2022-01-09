from requests import get, Session
from login import Login as ln
import json


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
        url = 'https://www.avanza.se/_cqbe/search/global-search/global-search-template?query=%s' % stock
        response = get(url, cookies=cookies).json()
        # response_dict = json.loads(response.json())
        return response
