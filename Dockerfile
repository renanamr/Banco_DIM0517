FROM python:3.11.3

WORKDIR /opt/app

COPY . .

ENV PYTHONPATH=/opt/app

CMD [ "python", "src/client/main.py"]
