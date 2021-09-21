# Author:
# License terms:

# python imports
import urllib

# project imports
from util import Util

POKEDEX_API = "https://pokeapi.co/api/v2/pokemon-species"
TRANSLATION_API = "https://api.funtranslations.com/translate/"


class PokemonFinder(Util):
    def __init__(self):
        pass

    # retrieve list of pokemon from the pokeapi
    def get_pokedex(self):
        """
        Function to obtain the list of pokemon from the pokemon api

        """
        list_of_pokemon = []
        total_pokemon = self.get_request(urllib.parse.urljoin(POKEDEX_API, "?limit=0"))["count"]
        poke_list = self.get_request(urllib.parse.urljoin(POKEDEX_API, f"?limit={total_pokemon}"))
        for pokemon in poke_list["results"]:
            list_of_pokemon.append(pokemon)
        return list_of_pokemon

    def get_pokemon_info(self):
        pass

    def translator(self):
        pass


if __name__ == "__main__":
    PokemonFinder().get_pokedex()
