"""
Програма для расчета по ДЗ №3
Версия 1.0
Автор: Андрей Корниенко

Домашнее задание
Тестирование API

Цель:
Поучиться тестировать API сервисов на основе их документации.

Тестирование каждого api оформить в отдельном тестовом модуле.

Тестирование REST сервиса 2
Написать минимум 5 тестов для REST API сервиса: https://www.openbrewerydb.org/.
Как минимум 2 из 5 должны использовать параметризацию.
Документация к API есть на сайте.
Тесты должны успешно проходить.

Критерии оценки:
Все перечисленные пункты сдавать одним pull-request'ом
Для всех файлов соблюдается минимальный код сатйл (встроенный форматтер PyCharm'а)
Под тесты каждого сервиса заведён отдельный файл
Рекомендуем сдать до: 28.07.2021"""

import requests
import pytest
from jsonschema import validate

# export PYTHONPATH="/Users/Andrey/Develop/homework3/"
from tests.test_jsonplaceholder_typicode_com.test_data.test_data import ids, userIds


def test_get_a_resource(base_url, http_method_get):
    target = base_url + "posts/1"
    response = http_method_get(url=target)
    response_json = response.json()

    assert response.status_code == 200
    assert len(response_json) == 4
    assert response_json['userId'] == 1
    assert response_json['id'] == 1
    assert response_json['title'] == 'sunt aut facere repellat provident occaecati excepturi ' \
                                     'optio reprehenderit'
    assert response_json['body'] == 'quia et suscipit\nsuscipit recusandae consequuntur expedita' \
                                    ' et cum\nreprehenderit molestiae ut ut quas totam\nnostrum ' \
                                    'rerum est autem sunt rem eveniet architecto'


def test_get_list_all_resources(base_url, http_method_get,
                                get_expected_list_all_resources_from_json_file):
    target = base_url + "posts"
    response = http_method_get(url=target)
    actual_list_all_resources = response.json()

    assert response.status_code == 200
    assert len(actual_list_all_resources) == 100
    assert get_expected_list_all_resources_from_json_file == actual_list_all_resources


@pytest.mark.parametrize("id_", ids)
def test_get_a_resource_json_schema_validation(base_url, http_method_get, id_):
    """Проверка структуры ответа на запрос /posts/{id_} с использованием 'jsonschema'"""

    target = base_url + f"posts/{id_}"
    response = http_method_get(url=target)

    assert response.status_code == 200

    schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "integer"},
            "id": {"type": "integer"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["userId", "id", "title", "body"]
    }

    validate(instance=response.json(), schema=schema)


def test_check_users_count(base_url, http_method_get):
    target = base_url + "users"
    response = http_method_get(url=target)

    assert response.status_code == 200
    assert len(response.json()) == 10


@pytest.mark.parametrize("userId", userIds)
def test_get_user_info_attr_count(base_url, http_method_get, userId):
    target = base_url + f"users/{userId}"
    response = http_method_get(url=target)

    assert response.status_code == 200
    assert response.json()["id"] == userId
    assert len(response.json()) == 8


@pytest.mark.parametrize("id_, name, username", [(1, "Leanne Graham", "Bret"),
                                                 (2, "Ervin Howell", "Antonette"),
                                                 (3, "Clementine Bauch", "Samantha"),
                                                 (4, "Patricia Lebsack", "Karianne"),
                                                 (5, "Chelsey Dietrich", "Kamren"),
                                                 (6, "Mrs. Dennis Schulist", "Leopoldo_Corkery"),
                                                 (7, "Kurtis Weissnat", "Elwyn.Skiles"),
                                                 (8, "Nicholas Runolfsdottir V", "Maxime_Nienow"),
                                                 (9, "Glenna Reichert", "Delphine"),
                                                 (10, "Clementina DuBuque", "Moriah.Stanton")
                                                 ])
def test_get_user_info_name(base_url, http_method_get, id_, name, username):
    target = base_url + f"users/{id_}"
    response = http_method_get(url=target)

    assert response.status_code == 200
    assert response.json()["id"] == id_
    assert response.json()["name"] == name
    assert response.json()["username"] == username


def test_create_a_resource(base_url, get_element_from_list_all_resources):
    target = base_url + "posts"
    data = get_element_from_list_all_resources

    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }

    response = requests.post(url=target, json=data, headers=headers)

    assert response.status_code == 201
    assert response.json()["id"] == 101
    assert response.json()["userId"] == get_element_from_list_all_resources["userId"]
    assert response.json()["body"] == get_element_from_list_all_resources["body"]
    assert response.json()["title"] == get_element_from_list_all_resources["title"]


@pytest.mark.parametrize("id_", [x for x in range(1, 101, 1)])
def test_update_a_resource(base_url, id_):
    target = base_url + f"posts/{id_}"

    data = {
        "id": id_,
        "title": "foo" + str(id_),
        "body": "bar" + str(id_),
        "userId": id_
    }

    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }

    response = requests.put(url=target, json=data, headers=headers)

    # print(f"\nresponse = {response}")
    # print(f"\nresponse.json() = {response.json()}")
    # print(f"\nresponse.ok = {response.ok}")
    # print(f"\nresponse.status_code = {response.status_code}")
    # print(f"\nresponse.headers = {response.headers}")
    # print(f"\nresponse.url = {response.url}")
    # print(f"\nresponse.content = {response.content}")
    # print(f"\nresponse.cookies = {response.cookies}")
    # print(f"\nresponse.next = {response.next}")

    assert response.ok
    assert response.json()["id"] == id_
    assert response.json()["userId"] == data["userId"]
    assert response.json()["body"] == data["body"]
    assert response.json()["title"] == data["title"]


@pytest.mark.parametrize("id_", [x for x in range(1, 101, 1)])
def test_patch_a_resource(base_url, id_):
    target = base_url + f"posts/{id_}"

    data = {
        "title": "foo" + str(id_)
    }

    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }

    response = requests.patch(url=target, json=data, headers=headers)

    assert response.status_code == 200
    assert response.json()["id"] == id_
    assert response.json()["title"] == data["title"]


@pytest.mark.parametrize("id_", [x for x in range(1, 101, 1)])
def test_delete_a_resource(base_url, id_):
    target = base_url + f"posts/{id_}"
    response = requests.delete(url=target)

    assert response.status_code == 200
    assert response.json() == {}
