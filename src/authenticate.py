from requests import post
from credentials import Credentials as cr
from paths import constants, BASE_URL


class Authenticate:
    def __init__(self) -> None:
        self.cookie
        self.authenticationTimeOut
        self.credentials

    def authenticate(self) -> dict:
        self.authenticationTimeout = 1440
        self.credentials = cr.loadCredentials()
        self.cookie = cr.loadCookie()

        data = {
            'maxInactiveMinutes': self.authenticationTimeout,
            'username': self.credentials['username'],
            'password': self.credentials['password']
        }

        url = f"{BASE_URL}{constants['paths']['AUTHENTICATION']}"
        response = post(url, data, cookies=self.cookies)
        return response.json
