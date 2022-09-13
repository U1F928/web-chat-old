FROM python:3.8.14-slim-bullseye

WORKDIR /web-chat

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "run.py"]