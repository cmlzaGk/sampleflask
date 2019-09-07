FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk add --update --no-cache \
           graphviz

ENV UWSGI_INI uwsgi.ini

ENV STATIC_URL /app/static/

ENV FLASK_CONFIG production

LABEL Name=demowebsite Version=0.0.1
ENV LISTEN_PORT=3000
EXPOSE 3000

WORKDIR /demowebserver
COPY bettermath-lib bettermath-lib
COPY randomweb-app randomweb-app
COPY requirements.txt uwsgi.ini ./

RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install  --no-deps bettermath-lib/
RUN python3 -m pip install  --no-deps randomweb-app/

