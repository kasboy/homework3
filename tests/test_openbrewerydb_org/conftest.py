import pytest

# export PYTHONPATH="/Users/Andrey/Develop/homework3/"
from tests.test_openbrewerydb_org.test_data.test_data import json_file_list_of_breweries_list


@pytest.fixture
def base_url():
    return "https://api.openbrewerydb.org/"


@pytest.fixture
def get_expected_json_breweries_list():
    return json_file_list_of_breweries_list
