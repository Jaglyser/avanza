from requests import Session, get
from src.credentials import Credentials as cr


class Login:
    def getCookie():
        csid = cr.loadCookie()
        cookies = {
            'csid': csid
        }
        return cookies
