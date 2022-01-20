FROM ubuntu:20.04
LABEL maintainer="e.gostyukhin@gmail.com"
RUN apt update -y
RUN apt install -y python3.8 python3.8-dev python3-pip build-essential
COPY . /src
WORKDIR /src
RUN python3 -m pip install -r requirements.txt
CMD ["uwsgi", "--http", "0.0.0.0:80", "--wsgi-file", "src/wsgi.py", "--callable", "app", "--stats", "0.0.0.0:81"]