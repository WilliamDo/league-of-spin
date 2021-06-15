FROM python:3

WORKDIR /usr/src/app

ADD leagueofspin leagueofspin
ADD leagues leagues
COPY manage.py ./

RUN pip install django==2.2
RUN pip install pyyaml
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py loaddata dev

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
