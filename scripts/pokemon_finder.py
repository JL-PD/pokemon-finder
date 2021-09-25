# Author:
# License terms:

# python imports
import urllib

# project imports
from util import Util

POKEDEX_API = "https://pokeapi.co/api/v2/pokemon-species"


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

    def get_pokemon_info(self, list_of_pokemon, pokemon_name: str):
        """
        Function to obtain and return required pokemon data: legendary status, habitat and descripton

        Keyword arguments:
        pokemon_name -- name of a pokemon
        """

        for i, pokemon in enumerate(list_of_pokemon):
            if pokemon_name == pokemon["name"]:
                pokemon_url = pokemon["url"]
                pokemon_data = self.get_request(pokemon_url)
                break
            if i == len(list_of_pokemon) - 1:
                print("Pokemon cannot be found in the Pokedex!")
                self.main()
        legendary_status = pokemon_data["is_legendary"]
        pokemon_habitat = pokemon_data["habitat"]["name"]

        for description in pokemon_data["flavor_text_entries"]:
            if description["language"]["name"] == "en":
                pokemon_description = description["flavor_text"]
                # break for performance, as we only care about the english translation
                break

        return legendary_status, pokemon_habitat, pokemon_description

    def translator(self):
        pass


if __name__ == "__main__":
    PokemonFinder().get_pokedex()
