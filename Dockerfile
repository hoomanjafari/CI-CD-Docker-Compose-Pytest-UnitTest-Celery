FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app


# because we're gonna use docker compose, we dont need this CMD command anymore
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
