# stateArt
## Project development in the backend directory
### LocalHost development
1. settings.py
```
DEBUG = True
```
2. .env
```
SECRET_KEY=django-secret-key
```
### Push git
1. settings.py
```
DEBUG = False
```
2. env
```
POSTGRES_DB=postgres_db
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=postgres_password
POSTGRES_HOST=postgres_host
POSTGRES_PORT=postgres_port
```
### Update requirements.txt
```
pip freeze > requirements.txt
```


