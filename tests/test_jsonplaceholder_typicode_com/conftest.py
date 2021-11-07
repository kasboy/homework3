import pytest

# export PYTHONPATH="/Users/Andrey/Develop/homework3/tests"
from test_jsonplaceholder_typicode_com.test_data.test_data import json_file_list_all_resources, element_from_list


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com/"


@pytest.fixture
def get_expected_list_all_resources_from_json_file():
    return json_file_list_all_resources


@pytest.fixture(params=element_from_list)
def get_element_from_list_all_resources(request):
    return request.param
