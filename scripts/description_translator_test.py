# python imports
import unittest
from unittest.mock import patch
import json

# project imports
from description_translator import DescriptionTranslator


mock_data = {"text": "This is a connection mock test"}


class TestDescriptionTranslator(unittest.TestCase):
    @patch("util.requests.post")
    def test_translator(self, mock_post_request):

        # testing legendary type pokemon: mewtwo
        legendary_status = True
        pokemon_habitat = "rare"
        pokemon_description = "mocked description"
        mock_post_request.return_value.text = json.dumps({"success": {"total": 1}, "contents": {"translated": "mocked translation", "text": "This is a connection mock test", "translation": "yoda"}})
        _, resp_type = DescriptionTranslator().translator(legendary_status, pokemon_habitat, pokemon_description)
        self.assertEqual(resp_type, "yoda")

        # testing cave habitat pokemon: zubat
        legendary_status = False
        pokemon_habitat = "cave"
        mock_post_request.return_value.text = json.dumps({"success": {"total": 1}, "contents": {"translated": "mocked translation", "text": "This is a connection mock test", "translation": "yoda"}})
        _, resp_type = DescriptionTranslator().translator(legendary_status, pokemon_habitat, pokemon_description)
        self.assertEqual(resp_type, "yoda")

        # testing non-legendary and non-cave habitat pokemon: pikachu
        legendary_status = False
        pokemon_habitat = "forest"
        mock_post_request.return_value.text = json.dumps({"success": {"total": 1}, "contents": {"translated": "mocked translation", "text": "This is a connection mock test", "translation": "yoda"}})
        _, resp_type = DescriptionTranslator().translator(legendary_status, pokemon_habitat, pokemon_description)
        self.assertEqual(resp_type, "shakespeare")
