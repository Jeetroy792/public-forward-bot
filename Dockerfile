FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app

CMD python3 main.py
RUN apt-get update && apt-get install -y ntpdate && ntpdate -s time.nist.gov
