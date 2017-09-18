FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /code/server
WORKDIR /code
ADD requirements.txt /code/server/
RUN pip install -r /code/server/requirements.txt
ADD . /code/