FROM python:3.8-slim-buster

ENV FASTAPI_HOST="0.0.0.0" \
    FASTAPI_PORT=5000 \
    FASTAPI_LOG_LEVEL="info"

EXPOSE $FASTAPI_PORT

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "./src/main.py"]