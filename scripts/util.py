import requests
from abc import abstractmethod

class Util:
    def __init__(self):
        pass

    def get_request(self, url):
        return requests.get(url).json()

    def post_request(self, url, data):
        pass
