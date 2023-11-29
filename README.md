# stateArt

### LocalHost development
1. settings.py
```
DEBUG = True
```
2. .env
```
SECRET_KEY=django-secret-key
```
### Deploy
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

RECAPTCHA_PUBLIC_KEY=RECAPTCHA_PUBLIC_KEY
RECAPTCHA_SECRET_KEY=RECAPTCHA_SECRET_KEY

EMAIL_HOST=EMAIL_HOST
EMAIL_PORT=EMAIL_PORT
EMAIL_HOST_USER=EMAIL_HOST_USER
EMAIL_HOST_PASSWORD=EMAIL_HOST_PASSWORD

EMAIL_RECIPIENT=EMAIL_RECIPIENT1,EMAIL_RECIPIENT2
```


### Update requirements.txt
```
pip freeze > requirements.txt
```


