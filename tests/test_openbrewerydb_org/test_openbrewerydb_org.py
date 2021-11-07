from datetime import datetime

import pytest
import cerberus
import jsonschema

# export PYTHONPATH="/Users/Andrey/Develop/homework3/tests"
from test_openbrewerydb_org.test_data.test_data import ids, cities


def test_get_list_breweries(base_url, http_method_get):
    target = base_url + "breweries"
    response = http_method_get(url=target)
    list_all_breweries = response.json()

    assert response.status_code == 200
    assert len(list_all_breweries) == 20


def test_compare_response_data_in_breweries_list(base_url, http_method_get,
                                                 get_expected_json_breweries_list):
    target = base_url + "breweries"
    response = http_method_get(url=target)
    actual_json_breweries_list = response.json()

    assert get_expected_json_breweries_list == actual_json_breweries_list


@pytest.mark.parametrize("city", cities)
def test_get_list_breweries_filtered_by_city_sep_by_(base_url, http_method_get, city):
    target = base_url + f"breweries?by_city={city.replace(' ', '_')}"
    response = http_method_get(url=target)

    assert response.status_code == 200
    assert response.json()
    assert response.json()[0]['city'] == city


@pytest.mark.parametrize("city", ["San Diego", "Castle Rock", "John Day", "Killeshin", "Gilbert"])
def test_get_list_breweries_filtered_by_city_sep_by_percent(base_url, http_method_get, city):
    target = base_url + f"breweries?by_city={city.replace(' ', '%20')}"
    response = http_method_get(url=target)

    assert response.status_code == 200
    assert response.json()
    assert response.json()[0]['city'] == city


@pytest.mark.parametrize("city", ["City One", "CityTwo", "City_Three", "City%20Four"])
def test_get_list_breweries_filtered_by_city_negative(base_url, http_method_get, city):
    target = base_url + f"breweries?by_city={city.replace(' ', '_')}"
    response = http_method_get(url=target)

    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.parametrize("name", ["cooper", "modern times", "dog", "cat", "north", "west",
                                  "12 gates"])
def test_get_list_breweries_filtered_by_name(base_url, http_method_get, name):
    target = base_url + f"breweries?by_name={name.replace(' ', '_')}"
    response = http_method_get(url=target)
    response_json = response.json()

    assert response.status_code == 200
    assert response_json

    for element in response_json:
        assert element["name"].lower().find(name) >= 0


@pytest.mark.parametrize("type_", ["micro", "nano", "regional", "brewpub", "large", "planning",
                                   "bar", "contract", "proprieter", "closed"])
def test_get_list_breweries_filtered_by_type(base_url, http_method_get, type_):
    target = base_url + f"breweries?by_type={type_}"
    response = http_method_get(url=target)
    response_json = response.json()

    assert response.status_code == 200
    assert response_json

    for element in response_json:
        assert element["brewery_type"].lower() == type_


@pytest.mark.parametrize("type_", ["micro_", "_nano", "regional_", "brew_pub", "large_new",
                                   "proprietor", "close"])
def test_get_list_breweries_filtered_by_type_negative(base_url, http_method_get, type_):
    target = base_url + f"breweries?by_type={type_}"
    response = http_method_get(url=target)
    response_json = response.json()

    assert response.status_code == 400
    assert response_json["errors"][0] == 'Brewery type must include one of these types: ["micro",' \
                                         ' "nano", "regional", "brewpub", "large", "planning", ' \
                                         '"bar", "contract", "proprieter", "closed"]'


@pytest.mark.parametrize("name", ["zzz", "VISKOSKOK", "666"])
def test_get_list_breweries_filtered_by_name_negative(base_url, http_method_get, name):
    target = base_url + f"breweries?by_name={name.replace(' ', '_')}"
    response = http_method_get(url=target)
    response_json = response.json()

    assert response.status_code == 200
    assert response_json == []


@pytest.mark.parametrize("id_", ids)
def test_get_single_brewery_json_schema_validation_cerberus(base_url, http_method_get, id_):
    """Проверка структуры ответа на запрос breweries/{id_} с использованием 'cerberus'"""

    target = base_url + f"breweries/{id_}"
    response = http_method_get(url=target)

    assert response.status_code == 200

    schema = {
        "id": {"required": True, "type": "string"},
        "name": {"required": True, "type": "string"},
        "brewery_type": {"required": True, "type": "string"},
        "street": {"required": True, "nullable": True, "type": "string"},
        "address_2": {"required": True, "nullable": True, "type": "string"},
        "address_3": {"required": True, "nullable": True, "type": "string"},
        "city": {"required": True, "type": "string"},
        "state": {"required": True, "nullable": True, "type": "string"},
        "county_province": {"required": True, "nullable": True, "type": "string"},
        "postal_code": {"required": True, "type": "string"},
        "country": {"required": True, "type": "string"},
        "longitude": {"required": True, "nullable": True, "type": "string"},  # "-86.627954",
        "latitude": {"required": True, "nullable": True, "type": "string"},  # "41.289715",
        "phone": {"required": True, "nullable": True, "type": "string"},
        "website_url": {"required": True, "nullable": True, "type": "string"},
        "updated_at": {"required": True, "type": "string"},  # "2021-10-23T02:24:55.243Z"
        "created_at": {"required": True, "type": "string"}  # "2021-10-23T02:24:55.243Z"
    }

    v = cerberus.Validator()
    res = v.validate(response.json(), schema)
    # print(f"res.errors={v.errors}")

    assert res


@pytest.mark.skip("Пример использования проверки json-схемы через 'jsonschema' (убран, т.к. в "
                  "генераторе будет 'stop iteration', если запускать совместно с тестом "
                  "'test_get_single_brewery_json_schema_validation_cerberus')")
@pytest.mark.parametrize("id_", ids)
def test_get_single_brewery_json_schema_validation_jsonschema(base_url, http_method_get, id_):
    """Проверка структуры ответа на запрос breweries/{id_} с использованием 'jsonschema'"""

    target = base_url + f"breweries/{id_}"
    response = http_method_get(url=target)
    assert response.status_code == 200

    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "brewery_type": {"type": "string"},
            "street": {
                "anyOf": [
                    {"type": "string"},
                    {"type": "null"}
                ]
            },
            "address_2": {
                "anyOf": [
                    {"type": "string"},
                    {"type": "null"}
                ]
            },
            "address_3": {
                "anyOf": [
                    {"type": "string"},
                    {"type": "null"}
                ]
            },
            "city": {"type": "string"},
            "state": {
                "anyOf": [
                    {"type": "string"},
                    {"type": "null"}
                ]
            },
            "county_province": {
                "anyOf": [
                    {"type": "string"},
                    {"type": "null"}
                ]
            },
            "postal_code": {"type": "string"},
            "country": {"type": "string"},
            "longitude": {
                "anyOf": [
                    {"type": "string"},
                    {"type": "null"}
                ]
            },  # "-86.627954",
            "latitude": {
                "anyOf": [
                    {"type": "string"},
                    {"type": "null"}
                ]
            },  # "41.289715",
            "phone": {"type": "string"},
            "website_url": {
                "anyOf": [
                    {"type": "string"},
                    {"type": "null"}
                ]
            },
            "updated_at": {"type": "string"},  # "2021-10-23T02:24:55.243Z"
            "created_at": {"type": "string"}  # "2021-10-23T02:24:55.243Z"
        },
        "required": ["id", "name", "brewery_type", "street", ]
    }

    def validate_with_datetime(schema, instance):
        """Add datetime validation to standard jsonschema validator"""

        BaseVal = jsonschema.Draft7Validator

        # Build a new type checker
        def is_datetime(checker, inst):
            return isinstance(inst, datetime)

        date_check = BaseVal.TYPE_CHECKER.redefine('datetime', is_datetime)

        # Build a validator with the new type checker
        Validator = jsonschema.validators.extend(BaseVal, type_checker=date_check)

        # Run the new Validator:
        Validator(schema=schema).validate(instance)

    validate_with_datetime(schema=schema, instance=response.json())
