FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /web/requirements.txt

WORKDIR /web

RUN pip install -r requirements.txt

COPY . /web

ENTRYPOINT [ "python" ]

CMD [ "web/run.py" ]