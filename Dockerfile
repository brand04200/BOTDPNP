FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app/discord

COPY discord/requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY discord/ ./

CMD ["python", "main.py"]
