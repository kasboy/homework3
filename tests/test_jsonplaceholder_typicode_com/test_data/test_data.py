import json


def get_list_all_resources_from_json_file():
    with open("./test_jsonplaceholder_typicode_com/test_data/list_all_resources.json", "r") as json_file:
        resources_list = json.loads(json_file.read())
        return resources_list


def get_ids_from_json_file():
    resources_list = get_list_all_resources_from_json_file()

    for element in resources_list:
        yield element['id']


def get_element_from_json_file():
    resources_list = get_list_all_resources_from_json_file()

    for element in resources_list:
        yield element


def get_userId_from_json_file():
    userIds_list = []
    resources_list = get_list_all_resources_from_json_file()

    for element in resources_list:
        userIds_list.append(element['userId'])

    unique_userIds_list = list(set(userIds_list))

    for userId in unique_userIds_list:
        yield userId


# Генератор
ids = get_ids_from_json_file()

# Генератор
userIds = get_userId_from_json_file()

# Генератор
element_from_list = get_element_from_json_file()

# Десериализованный Json-файл
json_file_list_all_resources = get_list_all_resources_from_json_file()
