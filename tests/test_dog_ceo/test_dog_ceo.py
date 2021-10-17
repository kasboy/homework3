import json
import collections
import pytest

from tests.test_dog_ceo.test_data.test_data import breeds


@pytest.mark.parametrize("image_count", [1, 3, 10, 25, 50])
def test_get_multiple_random_images(base_url, image_count, request_method):
    target = base_url + f"api/breeds/image/random/{image_count}"
    response = request_method(url=target)
    assert len(response.json()['message']) == image_count


@pytest.mark.parametrize("image_count", [-1, 0, 51])
def test_get_multiple_random_images_negative(base_url, image_count, request_method):
    target = base_url + f"api/breeds/image/random/{image_count}"
    response = request_method(url=target)

    with pytest.raises(AssertionError):
        assert len(response.json()['message']) == image_count


def test_check_all_main_breeds_count(base_url, request_method, get_dict_all_breeds):
    target = base_url + "api/breeds/list/all"
    response = request_method(url=target)

    assert response.status_code == 200
    assert get_dict_all_breeds['status'] == "success"
    assert len(get_dict_all_breeds['message']) == 94


@pytest.mark.skip("Оставил это для примера, сделал более короткий"
                  " тест 'test_check_all_items_in_dict_all_breeds'")
def test_check_items_in_list_all_breeds(get_dict_all_breeds):
    list_all_breeds_fact = []
    for key in get_dict_all_breeds['message'].keys():
        list_all_breeds_fact.append(key)

    list_all_breeds_expected = ['affenpinscher', 'african', 'airedale', 'akita', 'appenzeller',
                                'australian', 'basenji', 'beagle', 'bluetick', 'borzoi', 'bouvier',
                                'boxer', 'brabancon', 'briard', 'buhund', 'bulldog', 'bullterrier',
                                'cattledog', 'chihuahua', 'chow', 'clumber', 'cockapoo', 'collie',
                                'coonhound', 'corgi', 'cotondetulear', 'dachshund', 'dalmatian',
                                'dane', 'deerhound', 'dhole', 'dingo', 'doberman', 'elkhound',
                                'entlebucher', 'eskimo', 'finnish', 'frise', 'germanshepherd',
                                'greyhound', 'groenendael', 'havanese', 'hound', 'husky', 'keeshond',
                                'kelpie', 'komondor', 'kuvasz', 'labradoodle', 'labrador',
                                'leonberg', 'lhasa', 'malamute', 'malinois', 'maltese', 'mastiff',
                                'mexicanhairless', 'mix', 'mountain', 'newfoundland',
                                'otterhound', 'ovcharka', 'papillon', 'pekinese', 'pembroke',
                                'pinscher', 'pitbull', 'pointer', 'pomeranian', 'poodle', 'pug',
                                'puggle', 'pyrenees', 'redbone', 'retriever', 'ridgeback',
                                'rottweiler', 'saluki', 'samoyed', 'schipperke', 'schnauzer',
                                'setter', 'sheepdog', 'shiba', 'shihtzu', 'spaniel', 'springer',
                                'stbernard', 'terrier', 'vizsla', 'waterdog', 'weimaraner',
                                'wolfhound', 'whippet']

    # Сравниваем 2 списка (элементы в списках могут располагаться в разной последовательности)
    assert collections.Counter(list_all_breeds_fact) == collections.Counter(list_all_breeds_expected)


def test_check_all_items_in_dict_all_breeds(get_dict_all_breeds):
    with open("./test_data/list_all_breeds.json", "r") as json_file:
        dict_all_breeds_expected = json.loads(json_file.read())

    # Сравниваем 2 словаря (элементы в словарях могут располагаться в разной последовательности)
    assert get_dict_all_breeds['message'] == dict_all_breeds_expected


def test_get_breed_image_from_breed_list(base_url, request_method, get_breed_from_list):
    target = base_url + f"api/breed/{get_breed_from_list}/images/random"
    print(f"target = {target}")
    response = request_method(url=target)
    image_url = response.json()['message']
    response_image = request_method(url=image_url, stream=True)

    with open(f"./download_images/image_"
              f"{''.join(c if c != '/' else '_' for c in get_breed_from_list)}.jpg", "wb") as f:
        for chunk in response_image.iter_content(chunk_size=128):
            f.write(chunk)

    assert response.status_code == 200
    assert response_image.status_code == 200


# Вот так почему-то не работает параметризация, хотя 'breeds' - генератор. Брал это из примера
# тут: https://github.com/konflic/python_qa_ddt/blob/master/parametrization/test_param_gen.py
@pytest.mark.skip("Такой тест не работает, в 'breed_name' попадает пустой параметр")
@pytest.mark.parametrize("breed_name", breeds)
def test_get_breed_image_from_breed_list_2(base_url, request_method, breed_name):
    # print(f"breed_name = {breed_name}")
    target = base_url + f"api/breed/{breed_name}/images/random"
    # print(f"target = {target}")
    response = request_method(url=target)
    image_url = response.json()['message']
    response_image = request_method(url=image_url, stream=True)

    with open(f"./download_images/image_"
              f"{''.join(c if c != '/' else '_' for c in breed_name)}.jpg", "wb") as f:
        for chunk in response_image.iter_content(chunk_size=128):
            f.write(chunk)

    assert response.status_code == 200
    assert response_image.status_code == 200


def test_display_single_random_image(base_url, request_method):
    target = base_url + "api/breeds/image/random"
    response = request_method(url=target)
    random_image_url = response.json()['message']
    response_random_image = request_method(url=random_image_url)

    assert response.status_code == 200
    assert response_random_image.status_code == 200
    assert response.json()['status'] == "success"
