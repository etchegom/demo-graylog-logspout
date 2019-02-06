FROM python:3-alpine

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED=0

COPY app.py .

CMD ["python", "app.py"]
