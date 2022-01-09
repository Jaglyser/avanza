from requests import Session, get
from credentials import Credentials as cr


class Login:
    def getCookie():
        csid = cr.loadCookie()
        cookies = {
            'csid': csid
        }
        return cookies
        Session()
        url = 'https://www.avanza.se/min-profil/meddelanden.inkorg.471326716_471326716.html'
        r = get(url, cookies=cookies)
