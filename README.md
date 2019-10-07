QAPP project
===================
A project using Django and Django REST framework.

## Requirements
* You should have [virtualenv](http://www.virtualenv.org/en/latest/#installation) installed.

## Install
Set up and activate a virtualenv:
```console
virtualenv env
source env/bin/activate
```

Setup dependencies:
```console
make install
```

## Run the server
```console
make server
```
Launch [http://localhost:8000](http://localhost:8000) in your browser.

Default **username** is `admin` and **pasword** `qapp12345` .


**...in case** you'd like to start fresh:
```console
rm db.sqlite3
make initdb
```

...then head over to [Django admin](http://localhost:8000/admin/) and create your first client.

## Tests
```console
make test
```
