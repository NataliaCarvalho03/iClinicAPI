FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
EXPOSE 5000

RUN apt update
RUN apt install python3 pip -y

ADD . /app
WORKDIR /app
RUN pwd && ls -a
RUN pip install -r requirements.txt
ENTRYPOINT [ "python3.8" ]
CMD [ "main.py" ]