FROM python:3.10-alpine3.17

# Отключает сохранение кеша питоном
ENV PYTHONDONTWRITEBYTECODE 1
# Если проект крашнется, выведется сообщение из-за какой ошибки это произошло
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python ./manage.py collectstatic --noinput

CMD gunicorn stateArt.wsgi:application --bind 0.0.0.0:8000