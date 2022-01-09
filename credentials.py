from os import environ
from dotenv import load_dotenv


class Credentials:
    def loadCookie():
        load_dotenv()
        cookie = environ.get('CSID')
        return cookie
