FROM alpine:3.17 as builder
RUN apk add --no-cache gcc musl-dev

FROM python:3.8-alpine
COPY --from=builder /usr/bin/gcc /usr/bin/
COPY --from=builder /usr/lib/gcc /usr/lib/gcc
RUN apk add --no-cache libstdc++ build-base python3-dev bash

# #install python and pip
# RUN apk add --no-cache python3 python3-dev py3-pip build-base libffi-dev openssl-dev

RUN apk add ffmpeg

RUN pip install -U pip setuptools
RUN pip install wheel
RUN pip install --upgrade pip

COPY . /Algo_Web_Server

WORKDIR /Algo_Web_Server

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

# ENTRYPOINT [ "/bin/bash" ]
ENTRYPOINT [ "python", "-m", "./algo_server.py" ]
