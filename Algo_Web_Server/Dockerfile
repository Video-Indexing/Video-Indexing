FROM python:3.7-alpine

# #install python and pip
# RUN apk add --no-cache python3 python3-dev py3-pip build-base libffi-dev openssl-dev
RUN echo 'manylinux1_compatible = True' > /usr/local/lib/python3.7/site-packages/_manylinux.py 
RUN python -c 'import sys; sys.path.append(r"/_manylinux.py")' 

RUN apk add ffmpeg

RUN pip install -U pip setuptools
RUN pip install wheel
RUN pip install --upgrade pip

COPY / algo

WORKDIR /algo

RUN pip install -r requirements.txt
