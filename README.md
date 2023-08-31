# Django Auth & Object filter

### This Project:

- Authentication (register and login).
- CRUD on the enterprise model and filtering the enterprises.
- Following and listing of follow-ups.

# How to Install

### Create a virtual environment:

`python3 -m venv env`

### Activate the virtual environment:

`source env/bin/activate`

### Install requirements:

`pip3 install -r requirements.txt`

### Create a environment file in the BASE_DIR named .env and put the informations:

```
touch .env
```
```
DEBUG=True
SECRET_KEY=<secret-key>
POSTGRES_DB=<db-name>
POSTGRES_USER=<db-user>
POSTGRES_PASSWORD=<db-password>
DATABASE_HOST=<db-host>
DATABASE_PORT=5432
```

### Make migrations for database tables creating:

`python3 manage.py makemigrations`

### Migrate:

`python3 manage.py migrate`

### Create a superuser for app management:

`python3 manage.py createsuperuser`

## Run the server:

`python3 manage.py runserver`

# Run the Unittest for project

## on the main folder of project run this command

`python3 manage.py test`

# Create the User and Kurulus objects using command

## Create User:

`python3 manage.py create_user`

## Create Kurulus:

`python3 manage.py populatedata`
