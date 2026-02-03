import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


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
