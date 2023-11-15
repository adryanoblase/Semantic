# Dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY semantic.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "semantic.py"]
