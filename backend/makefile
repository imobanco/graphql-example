up: migrate
	python manage.py runserver

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

poetry.install:
	poetry config virtualenvs.in-project true
	poetry config virtualenvs.path .
	poetry install
