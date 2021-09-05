FROM python:3.6-stretch
RUN apt update && apt install -y python3-dev
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
WORKDIR /code/
EXPOSE 8000
