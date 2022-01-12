from authenticate import Authenticate as auth
from avanzasocket import AvanzaSocket


class Client:
    def __init__(self) -> None:
        self.response, self.credentials, self.cookie = auth.authenticate()
        self.socket = AvanzaSocket()
