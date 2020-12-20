FROM python:3.7-slim-buster
WORKDIR /code
RUN apt-get update
 

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python","-u","auto.py"]