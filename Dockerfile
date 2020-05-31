FROM python:3.8

RUN pip install pipenv

WORKDIR /app/web

ADD Pipfile Pipfile

ADD Pipfile.lock Pipfile.lock

RUN pipenv install --system --skip-lock

RUN pip install gunicorn[gevent]

ADD . /app

ADD ./convo /app/web/convo

EXPOSE 5000

CMD gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:$PORT app:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info