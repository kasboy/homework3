import pytest
import requests


@pytest.fixture
def http_method_get():
    return getattr(requests, "get")
