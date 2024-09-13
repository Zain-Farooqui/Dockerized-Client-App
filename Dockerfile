# Client Dockerfile
FROM python:3.9-slim

WORKDIR /app

RUN apt update
RUN apt upgrade -y
RUN apt install python3-pip -y
RUN pip install requests

# Copy client script
COPY client_app.py /app

CMD ["python", "client_app.py"]
