FROM python:3.8.14-slim-bullseye

WORKDIR /web-chat

COPY . .

RUN pip3 install -r requirements.txt

CMD [ "python3", "run.py"]