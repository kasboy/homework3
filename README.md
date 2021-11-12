# homework3
Repository for homework3

Before run tests: 
   
    1. Export env variable:
    export PYTHONPATH="/Users/Andrey/Develop/homework3/"

    2. Run tests
    pytest -vs tests/
    pytest -vs tests/test_check_response_status_code
    pytest -vs tests/test_dog_seo
    pytest -vs tests/test_dog_seo/test_dog_ceo.py
    pytest -vs tests/test_dog_ceo/test_dog_ceo.py::est_get_multiple_random_images     

Or run tests like this:
PYTHONPATH="/Users/Andrey/Develop/homework3/ pytest -vs tests/