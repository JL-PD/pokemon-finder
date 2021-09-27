import unittest
from pokemon_finder import PokemonFinder
from util import Util

# Utility
class TestPokemonFinder(unittest.TestCase, Util):
    def test_get_pokedex(self):
        # Using greater than to avoid false positives in the case that the pokemon list expands
        self.assertGreaterEqual(len(PokemonFinder.get_pokedex(self)), 898)

    def test_get_pokemon_info(self):
        list_of_pokemon = [
            {"name": "bulbasaur", "url": "https://pokeapi.co/api/v2/pokemon-species/1/"},
            {"name": "ivysaur", "url": "https://pokeapi.co/api/v2/pokemon-species/2/"},
            {"name": "venusaur", "url": "https://pokeapi.co/api/v2/pokemon-species/3/"},
            {"name": "charmander", "url": "https://pokeapi.co/api/v2/pokemon-species/4/"},
            {"name": "charmeleon", "url": "https://pokeapi.co/api/v2/pokemon-species/5/"},
        ]
        # existing pokemon: bulbasaur
        legendary_status, pokemon_habitat, pokemon_description = PokemonFinder.get_pokemon_info(self, list_of_pokemon, "bulbasaur")
        self.assertEqual(legendary_status, False)
        self.assertEqual(pokemon_habitat, "grassland")
        self.assertEqual(pokemon_description, "A strange seed was\nplanted on its\nback at birth.\x0cThe plant sprouts\nand grows with\nthis POKéMON.")

        # non existing pokemon : blue eyes white dragon
        # to stop the get_pokemon_info function from looping when an incorrect pokemon is inserted.
        # instead we call exit and check that the self.main is called.
        print("Blue Eyes White Dragon")
        legendary_status, pokemon_habitat, pokemon_description = PokemonFinder.get_pokemon_info(self, list_of_pokemon, "blue eyes white dragon")
        self.assertEqual(legendary_status, None)
        self.assertEqual(pokemon_habitat, None)
        self.assertEqual(pokemon_description, None)
        # incorrect input type : integer
        print("integer input")
        legendary_status, pokemon_habitat, pokemon_description = PokemonFinder.get_pokemon_info(self, list_of_pokemon, 121317231)
        self.assertEqual(legendary_status, None)
        self.assertEqual(pokemon_habitat, None)
        self.assertEqual(pokemon_description, None)
