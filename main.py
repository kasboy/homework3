import requests
import pytest

proxy = {"http": "localhost:8080", "https": "localhost:8080"}
response = requests.get('https://ya.ru', proxies=proxy, verify=False)
print(f"response = {response}")
assert response.status_code == 200

print(f"response.headers.items() = {response.headers.items()}")
print(f"response.headers.items() = {response.headers.items()}")

print(100 * '*')
for key, value in response.headers.items():
    print(key, '=>', value)
