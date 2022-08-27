up: migrate
	python manage.py runserver

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

fmt:
	isort .
	black .
	make fmt.check

fmt.check:
	isort --check-only .
	black --check .

poetry.install:
	poetry config virtualenvs.in-project true
	poetry config virtualenvs.path .
	poetry install

dumpdata:
	-mkdir core/fixtures
	python manage.py dumpdata --format=json $(app)$(model) > core/fixtures/initial_$(app)$(model).json

populate.superuser:
	python manage.py loaddata initial_superuser.json
