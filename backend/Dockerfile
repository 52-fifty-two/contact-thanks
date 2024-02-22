FROM python:3.10

ENV APP_HOME /app

WORKDIR $APP_HOME

RUN apt-get update && apt-get install -y --allow-unauthenticated vim

COPY requirements.txt $APP_HOME

RUN pip3 install --root-user-action=ignore -r requirements.txt

COPY . $APP_HOME

CMD ["python3", "manage.py"]
