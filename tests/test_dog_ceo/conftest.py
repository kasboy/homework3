import pytest

from tests.test_dog_ceo.test_data.test_data import breeds


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://dog.ceo/",
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
def get_dict_all_breeds(base_url, request_method):
    target = base_url + "api/breeds/list/all"
    response = request_method(url=target)
    dict_all_breeds = response.json()
    return dict_all_breeds


# Пример использования параметров из файла ('breeds' - генератор)
@pytest.fixture(params=breeds)
def get_breed_from_list(request):
    print(f"request.param = {request.param}")
    return request.param


# # Пример использования параметризации фикстуры списком значений
# @pytest.fixture(params=['affenpinscher', 'african', 'airedale', 'akita', 'appenzeller',
#                         'australian', 'basenji', 'beagle', 'bluetick', 'borzoi', 'bouvier',
#                         'boxer', 'brabancon', 'briard', 'buhund', 'bulldog', 'bullterrier',
#                         'cattledog', 'chihuahua', 'chow', 'clumber', 'cockapoo', 'collie',
#                         'coonhound', 'corgi', 'cotondetulear', 'dachshund', 'dalmatian',
#                         'dane', 'deerhound', 'dhole', 'dingo', 'doberman', 'elkhound',
#                         'entlebucher', 'eskimo', 'finnish', 'frise', 'germanshepherd',
#                         'greyhound', 'groenendael', 'havanese', 'hound', 'husky', 'keeshond',
#                         'kelpie', 'komondor', 'kuvasz', 'labradoodle', 'labrador',
#                         'leonberg', 'lhasa', 'malamute', 'malinois', 'maltese', 'mastiff',
#                         'mexicanhairless', 'mix', 'mountain', 'newfoundland', 'otterhound',
#                         'ovcharka', 'papillon', 'pekinese', 'pembroke', 'pinscher', 'pitbull',
#                         'pointer', 'pomeranian', 'poodle', 'pug', 'puggle', 'pyrenees', 'redbone',
#                         'retriever', 'ridgeback', 'rottweiler', 'saluki', 'samoyed', 'schipperke',
#                         'schnauzer', 'setter', 'sheepdog', 'shiba', 'shihtzu', 'spaniel', 'springer',
#                         'stbernard', 'terrier', 'vizsla', 'waterdog', 'weimaraner', 'whippet',
#                         'wolfhound'])
# def get_breed_from_list_(request):
#     return request.param
