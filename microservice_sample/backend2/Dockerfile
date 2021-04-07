FROM alpine:3.8

RUN apk add --no-cache py3-pip python3 && \
    pip3 install flask

COPY . /usr/src/backend2

ENV FLASK_APP backend2.py

WORKDIR /usr/src/backend2

CMD flask run --host=0.0.0.0 --port=5100
