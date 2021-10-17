import json


def get_breeds():
    breeds_list = []
    i = 0
    with open("./test_data/list_all_breeds.json", "r") as json_file:
        breeds_dict = json.loads(json_file.read())
        for key, value in breeds_dict.items():
            if len(value) > 0:
                for el in range(len(value)):
                    breeds_list.append('/'.join([key, value[el]]))
            else:
                breeds_list.append(str(key))

    for breed in breeds_list:
        yield breed


# Генератор
breeds = get_breeds()

# for breed in breeds:
#     print(f"breed={breed}")
