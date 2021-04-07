FROM alpine:3.8

RUN apk add --no-cache py3-pip python3 && \
    pip3 install flask requests

COPY . /usr/src/frontend2

ENV FLASK_APP frontend2.py

WORKDIR /usr/src/frontend2

CMD flask run --host=0.0.0.0 --port=8100
