FROM python:3.11.3

WORKDIR /server

COPY src/server/requirements.txt .

RUN pip install -r requirements.txt

COPY src/server/ .

EXPOSE 5000

ENV FLASK_APP=main.py
ENV PYTHONPATH=/server

CMD ["flask", "run", "--host=0.0.0.0"]