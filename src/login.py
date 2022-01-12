from requests import Session, get
from credentials import Credentials as cr


class Login:
    def getCookie():
        csid = cr.loadCookie()
        cookies = {
            'csid': csid
        }
        return cookies
