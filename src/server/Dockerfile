FROM python:3.11.3

RUN pip install flask 

WORKDIR /server

COPY . .

EXPOSE 5000

ENV FLASK_APP=main.py
CMD ["flask", "run", "--host=0.0.0.0"]