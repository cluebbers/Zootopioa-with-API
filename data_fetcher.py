import requests

API_KEY = "e7svScyqfFPWDxqYWSHb9it5FqT2jPdG9WAJsHTO"


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    },
    """
    animals_url = "https://api.api-ninjas.com/v1/animals"
    params = {"name": animal_name, "X-Api-Key": API_KEY}
    fox_info = requests.get(animals_url, params=params)
    return fox_info.json()
