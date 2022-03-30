FROM python:3.8-slim-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
