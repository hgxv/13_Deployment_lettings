FROM python:3.11.5
ENV PYTHONUNBUFFERED 1
ENV PORT 8000
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
CMD \
    python3 manage.py collectstatics --noinput && \
    python3 manage.py runserver 0.0.0.0:$PORT
