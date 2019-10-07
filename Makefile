initdb:
	python manage.py makemigrations
	python manage.py migrate

install:
	pip install -r requirements.txt

test:
	python manage.py test --verbosity 2

server:
	python manage.py runserver 0.0.0.0:8000