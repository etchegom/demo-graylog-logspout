FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt && rm -f requirements.txt

ENV PYTHONUNBUFFERED=0

COPY app.py .

CMD ["python", "app.py"]
