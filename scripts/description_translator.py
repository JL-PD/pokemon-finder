import json
from util import Util
import urllib

TRANSLATION_API = "https://api.funtranslations.com/translate/"


class DescriptionTranslator(Util):
    def __init__(self):
        pass

    def translator(self, legendary_status, pokemon_habitat, pokemon_description):
        """
        Function to select which translator to use depending on the pokemon's legendary status or pokemon habitat
        and return a suitable description based on the legendary status or pokemon habitat

        Keyword arguments:
        legendary_status -- legendary status of pokemon
        pokemon_habitat -- habitat of pokemon
        pokemon_description -- description about the pokemon

        """

        data = {"text": pokemon_description}

        if pokemon_habitat == "cave" or legendary_status == True:
            post_translation = json.loads(self.post_request(urllib.parse.urljoin(TRANSLATION_API, "yoda.json"), data=data).text)
            post_translation.update({"translation_type": "yoda"})
        else:
            post_translation = json.loads(self.post_request(urllib.parse.urljoin(TRANSLATION_API, "shakespeare.json"), data=data).text)
            post_translation.update({"translation_type": "shakespeare"})
        try:
            translation = post_translation["contents"]["translated"]
            translation_type = post_translation["translation_type"]
            return translation, translation_type
        except KeyError:
            # the api has a 5 request limit per hour, return error message if limit is reached
            formatted_description = pokemon_description.replace("\n", " ")
            return f'{post_translation["error"]["message"]} Returning untranslated description:\n{formatted_description}', None
