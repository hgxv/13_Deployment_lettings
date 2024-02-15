FROM python:3.11
ENV PYTHONUNBUFFERED 1
ENV PORT 8000
WORKDIR /app
COPY . .
COPY .env .
RUN pip install -r requirements.txt
CMD \
    python3 manage.py collectstatic --noinput && \
    python3 manage.py runserver 0.0.0.0:$PORT
