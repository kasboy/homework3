"""
Програма для расчета по ДЗ №3
Версия 1.0
Автор: Андрей Корниенко

Домашнее задание
Тестирование API

Цель:
Поучиться тестировать API сервисов на основе их документации.

Тестирование каждого api оформить в отдельном тестовом модуле.

Реализуйте в отдельном модуле (файле) тестовую функцию которая будет принимать 2 параметра:
url - должно быть значение по умолчанию https://ya.ru
status_code - значение по умолчанию 200
Параметры должны быть реализованы через pytest.addoption.
Можно положить фикcтуру и тестовую функцию в один файл.
Основная задача чтобы ваш тест проверял по переданному урлу статус ответа тот который передали,
т.е. по адресу https://ya.ru/sfhfhfhfhfhfhfhfh должен быть валидным ответ 404

пример запуска pytest test_module.py --url=https://mail.ru --status_code=200

Критерии оценки:
Все перечисленные пункты сдавать одним pull-request'ом
Для всех файлов соблюдается минимальный код сатйл (встроенный форматтер PyCharm'а)
Под тесты каждого сервиса заведён отдельный файл
Рекомендуем сдать до: 28.07.2021"""

import pytest


def test_url_status(base_url, status_code, request_method):
    """Тестовая функция для проверки работы параметров, переданных в виде аргументов 'pytest'
    Пример запуска: pytest test_check_response_status_code.py::test_url_status
    --url=https://mail.ru --status_code=200"""

    target = base_url
    response = request_method(url=target)

    assert str(response.status_code) == status_code


@pytest.mark.parametrize("status_code", [200, 300, 400, 404, 500, 502])
def test_url_status_test(request_method, status_code):
    """Тест для проверки корректности работы проверки кодов ответа без 'pytest.addoption.' с
     использованием тестового ресурса https://httpbin.org."""

    target = f"https://httpbin.org/status/{status_code}"
    response = request_method(url=target)

    assert response.status_code == status_code
