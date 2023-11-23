﻿# stateArt

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
```


### Update requirements.txt
```
pip freeze > requirements.txt
```


