import pytest
import requests


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://httpbin.org/",  # https://httpbin.org/ https://ya.ru/
        help="This is request url"
    )

    parser.addoption(
        "--status_code",
        default='200',
        choices=['200', '300', '400', '404', '500', '502'],  # https://httpbin.org/status/404
        help="This is response status code"
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
def status_code(request):
    return request.config.getoption("--status_code")


@pytest.fixture
def request_method(request):
    return getattr(requests, request.config.getoption("--method"))


@pytest.fixture
def http_method_get():
    return getattr(requests, "get")
