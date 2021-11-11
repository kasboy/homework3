import json
from pathlib import Path


CUR_DIR = Path(__file__).parent

def get_json_file_list_of_breweries_list():
    with open(f"{CUR_DIR}/list_of_breweries.json", "r") as json_file:
        breweries_list = json.loads(json_file.read())
        return breweries_list


def get_brewerie_cities_from_json():
    brewerie_cities_list = []
    breweries_list = get_json_file_list_of_breweries_list()

    for element in breweries_list:
        brewerie_cities_list.append(element['city'])

    unique_breweries_list = list(set(brewerie_cities_list))
    for element in unique_breweries_list:
        yield element


def get_brewerie_id_from_json():
    breweries_list = get_json_file_list_of_breweries_list()

    for element in breweries_list:
        yield element['id']


# Генератор
cities = get_brewerie_cities_from_json()

# Генератор
ids = get_brewerie_id_from_json()

# Десериализованный Json-файл
json_file_list_of_breweries_list = get_json_file_list_of_breweries_list()
