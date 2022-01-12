import websocket
import _thread
import time
from paths import SOCKET_URL
from login import Login as ln
from credentials import Credentials as cr
import json
import Session from requests

message_count = 0


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print('error:')
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def callback(data):
    print(data)


def on_open(ws):

    # hs =
    # {
    #     'channel': '/meta/connect',

    # }

    message = {
        "channel": "/meta/subscribe",
        "clientId":  None,
        "subscription": '/quotes/5364'
    }

    ws.send(json.dumps(message))
    # ws.send(json.dumps(hs))


if __name__ == "__main__":
    cookie = "csid=%s" % cr.loadCookie()
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(SOCKET_URL,
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close,
                                cookie=cookie)
    ws.run_forever()
