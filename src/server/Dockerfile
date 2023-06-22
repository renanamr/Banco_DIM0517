FROM python:3.11.3

RUN pip install flask 
RUN pip install pytest

WORKDIR /server

COPY . .

EXPOSE 5000

ENV FLASK_APP=main.py
ENV PYTHONPATH=/server
CMD ["flask", "run", "--host=0.0.0.0"]