FROM python:3.12-bullseye

RUN apt-get update && apt-get install -y git

RUN python -m pip install --upgrade pip

WORKDIR /elif

COPY . /elif

RUN pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE=elif.settings

ENV DAPHNE_PORT=2002

ENV APP_ASGI_ENTRYPOINT=elif.asgi:application

EXPOSE 2002

RUN python /elif/manage.py migrate

RUN python /elif/manage.py loaddata initial_data.json

CMD ["daphne", "-b", "0.0.0.0", "-p", "2002", "elif.asgi:application"]
