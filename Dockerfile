FROM python:3

WORKDIR /usr/src/app

COPY leagueofspin ./
COPY leagues ./
COPY manage.py ./

RUN pip install django==2.2
RUN python manage.py makemigrations leagues
RUN python manage.py migrate
RUN python manage.py loaddata dev

CMD ["python", "manage.py", "runserver"]
