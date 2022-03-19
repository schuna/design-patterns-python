ECHO pytest
python -m unittest discover .
pytest --cov-report term-missing --cov=src tests
ECHO coverage
coverage run -m unittest discover
coverage report -m
coverage html
