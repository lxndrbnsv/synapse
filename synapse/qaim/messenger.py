import requests


class RedirectMessageTest:
    def __init__(self, data):
        requests.post("https://m.qaim.me/api/test_receive_incoming_data", json=data)
