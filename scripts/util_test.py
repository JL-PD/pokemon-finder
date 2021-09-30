# python imports
import unittest
import requests

POKEDEX_API = "https://pokeapi.co/api/v2/pokemon-species"
SHAKESPEARE_API = "https://api.funtranslations.com/translate/shakespeare.json"


class TestUtil(unittest.TestCase):
    def test_get_requests(self):
        r = requests.get(POKEDEX_API)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 4)

    def test_post_request(self):
        data = {"text": "This is a connection test"}
        r = requests.post(SHAKESPEARE_API, json=data)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 2)
