import json
import requests

APININJA_KEY = "e7svScyqfFPWDxqYWSHb9it5FqT2jPdG9WAJsHTO"


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def load_api_data(name="fox"):
    """
    Fetches animal information from api-ninjas

    args
     name (str): name of the animal, default 'fox'
    returns
        json: document about all animals with name
    """
    animals_url = "https://api.api-ninjas.com/v1/animals"
    params = {"name": name, "X-Api-Key": APININJA_KEY}
    fox_info = requests.get(animals_url, params=params)

    return fox_info.json()


def serialize_animal(animal_obj):
    """Serializes an animal object into HTML format"""
    output = ""
    output = '<li class="cards__item">\n'
    if "name" in animal_obj:
        output += f'  <div class="card__title">{animal_obj["name"]}</div>\n'
    output += '  <div class="card__text">\n'
    output += "    <ul>"
    if "diet" in animal_obj["characteristics"]:
        output += f'      <li><strong>Diet:</strong> {animal_obj["characteristics"]["diet"]}</li>\n'
    if "locations" in animal_obj:
        output += f'      <li><strong>Location:</strong> {", ".join(animal_obj["locations"])}</li>\n'
    if "type" in animal_obj["characteristics"]:
        output += f'      <li><strong>Type:</strong> {animal_obj["characteristics"]["type"]}</li>\n'
    output += "    </ul>\n"
    output += "  </div>\n"
    output += "</li>\n"
    return output


def load_template(file_path):
    """Loads an HTML template file"""
    with open(file_path, "r") as template:
        return template.read()


def write_output(file_path, content):
    """Writes content to an output file"""
    with open(file_path, "w") as output_file:
        output_file.write(content)


def main():
    # animals_data = load_data("animals_data.json")
    animal_name = input('Enter a name of an animal: ')
    animals_data = load_api_data(name=animal_name)

    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)

    template = load_template("animals_template.html")

    template = template.replace("__REPLACE_ANIMALS_INFO__", output)

    write_output("animals.html", template)
    print('Website was successfully generated to the file animals.html.')


if __name__ == "__main__":
    main()
