from os import environ
from dotenv import load_dotenv


class Credentials:
    def loadCookie() -> str:
        load_dotenv()
        cookie = environ.get('CSID')
        return cookie

    def loadCredentials() -> dict:
        load_dotenv()
        credentials = {
            'username': environ.get('username'),
            'password': environ.get('password'),
            'totp': environ.get('totp')
        }
        return credentials
