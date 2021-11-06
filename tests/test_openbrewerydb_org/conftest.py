import pytest
import requests


# export PYTHONPATH="/Users/Andrey/Develop/homework3/tests/test_openbrewerydb_org"
from test_data.test_data import json_file_list_of_breweries_list


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://api.openbrewerydb.org/",
        help="This is request url"
    )

    parser.addoption(
        "--method",
        default="get",
        choices=["get", "post", "put", "patch", "delete"],
        help="method to execute"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def request_method(request):
    return getattr(requests, request.config.getoption("--method"))


@pytest.fixture
def get_expected_json_breweries_list():
    return json_file_list_of_breweries_list
