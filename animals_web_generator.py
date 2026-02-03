import json

import data_fetcher


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


def create_html(output):
    """write an html file according to the template and output

    Args:
        output (html): html with animal information
    """
    template = load_template("animals_template.html")
    template = template.replace("__REPLACE_ANIMALS_INFO__", output)
    write_output("animals.html", template)
    print("Website was successfully generated to the file animals.html.")


def main():

    animal_name = input("Enter a name of an animal: ")
    animals_data = data_fetcher.fetch_data(animal_name)

    output = ""
    for animal in animals_data:
        output += serialize_animal(animal)
    if output == "":
        output = f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'
    create_html(output)


if __name__ == "__main__":
    main()
