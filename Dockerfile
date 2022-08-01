FROM python:3.9.13-alpine3.15 as build

RUN apk add --no-cache gcc musl-dev build-base

WORKDIR /usr/local/src/website

COPY ./themes ./themes
COPY ./content ./content
COPY ./requirements.txt ./requirements.txt
COPY ./pelicanconf.py ./pelicanconf.py
COPY ./publishconf.py ./publishconf.py

RUN python3 -m venv venv
RUN source ./venv/bin/activate
RUN pip install -r requirements.txt
RUN pelican content -s publishconf.py

FROM caddy:2-alpine

COPY --from=build /usr/local/src/website/build /srv/www
COPY Caddyfile /etc/caddy/Caddyfile