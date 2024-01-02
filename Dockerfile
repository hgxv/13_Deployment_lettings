FROM python:3.11.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD . /app/
CMD python3 manage.py runserver 0.0.0.0:8000
